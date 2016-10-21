# coding: utf-8
# Copyright (c) Pymatgen Development Team.
# Distributed under the terms of the MIT License.

from __future__ import division, unicode_literals

"""
Created on Apr 17, 2012
"""


__author__ = "Shyue Ping Ong"
__copyright__ = "Copyright 2012, The Materials Project"
__version__ = "0.1"
__maintainer__ = "Shyue Ping Ong"
__email__ = "shyuep@gmail.com"
__date__ = "Apr 17, 2012"

import unittest2 as unittest
import os

from pymatgen import Molecule
from pymatgen.io.gaussian import GaussianInput, GaussianOutput
<<<<<<< HEAD
=======
from pymatgen.electronic_structure.core import Spin
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b

test_dir = os.path.join(os.path.dirname(__file__), "..", "..", "..",
                        'test_files', "molecules")


class GaussianInputTest(unittest.TestCase):

    def setUp(self):

        coords = [[0.000000, 0.000000, 0.000000],
                  [0.000000, 0.000000, 1.089000],
                  [1.026719, 0.000000, -0.363000],
                  [-0.513360, -0.889165, -0.363000],
                  [-0.513360, 0.889165, -0.363000]]
        self.coords = coords
        mol = Molecule(["C", "H", "H", "H", "H"], coords)
        self.gau = GaussianInput(
            mol, route_parameters={'SP': "", "SCF": "Tight"},
            input_parameters={"EPS": 12})

    def test_init(self):
        mol = Molecule(["C", "H", "H", "H", "H"], self.coords)
        gau = GaussianInput(mol, charge=1, route_parameters={'SP': "",
                                                             "SCF": "Tight"})
        self.assertEqual(gau.spin_multiplicity, 2)
        mol = Molecule(["C", "H", "H", "H", "H"], self.coords, charge=-1)
        gau = GaussianInput(mol, route_parameters={'SP': "", "SCF": "Tight"})
        self.assertEqual(gau.spin_multiplicity, 2)
        self.assertRaises(ValueError, GaussianInput, mol, spin_multiplicity=1)

    def test_str_and_from_string(self):
        ans = """#P HF/6-31G(d) SCF=Tight SP

H4 C1

0 1
C
H 1 B1
H 1 B2 2 A2
H 1 B3 2 A3 3 D3
H 1 B4 2 A4 4 D4

B1=1.089000
B2=1.089000
A2=109.471221
B3=1.089000
A3=109.471213
D3=120.000017
B4=1.089000
A4=109.471213
D4=119.999966

EPS=12

"""
        self.assertEqual(str(self.gau), ans)
        gau = GaussianInput.from_string(ans)
        self.assertEqual(gau.functional, 'HF')
        self.assertEqual(gau.input_parameters['EPS'], '12')

    def test_from_file(self):
        filepath = os.path.join(test_dir, 'MethylPyrrolidine_drawn.gjf')
        gau = GaussianInput.from_file(filepath)
        self.assertEqual(gau.molecule.composition.formula, "H11 C5 N1")
        self.assertIn("opt", gau.route_parameters)
        self.assertEqual(gau.route_parameters["geom"], "connectivity")
        self.assertEqual(gau.functional, "b3lyp")
        self.assertEqual(gau.basis_set, "6-311+g(d,p)")
        filepath = os.path.join(test_dir, "g305_hb.txt")
        with open(filepath) as f:
            txt = f.read()
        toks = txt.split("--link1--")
        for i, t in enumerate(toks):
            lines = t.strip().split("\n")
            lines = [l.strip() for l in lines]
            gau = GaussianInput.from_string("\n".join(lines))
            self.assertIsNotNone(gau.molecule)
            if i == 0:
                mol = gau.molecule
        ans = """Full Formula (H4 O2)
Reduced Formula: H2O
Charge = 0, Spin Mult = 1
Sites (6)
0 O     0.000000     0.000000     0.000000
1 O     0.000000     0.000000     2.912902
2 H     0.892596     0.000000    -0.373266
3 H     0.143970     0.000219     0.964351
4 H    -0.582554     0.765401     3.042783
5 H    -0.580711    -0.766761     3.043012"""
        self.assertEqual(str(mol), ans)

    def test_from_string(self):
        gau_str = """%mem=5000000
        %chk=filename
        # mp2/6-31g* scf=direct

        SIH4+ H2---SIH2+ CS //MP2(full)/6-31G* MP2=-290.9225259

        1,2
        Si
        X,1,1.
        H,1,R1,2,HALF1
        H,1,R1,2,HALF1,3,180.,0
        X,1,1.,2,90.,3,90.,0
        X,1,1.,5,THETA,2,180.,0
        H,1,R3,6,HALF3,5,0.,0
        H,1,R4,6,HALF3,7,180.,0

        R1=1.47014
        R3=1.890457
        R4=1.83514
        HALF1=60.633314
        THETA=10.35464
        HALF3=11.861807"""

        gau = GaussianInput.from_string(gau_str)
        self.assertEqual("X3SiH4", gau.molecule.composition.reduced_formula)

    def test_gen_basis(self):
        gau_str = """#N B3LYP/Gen Pseudo=Read

Test

0 1
C
H 1 B1
H 1 B2 2 A2
H 1 B3 2 A3 3 D3
H 1 B4 2 A4 4 D4

B1=1.089000
B2=1.089000
A2=109.471221
B3=1.089000
A3=109.471213
D3=120.000017
B4=1.089000
A4=109.471213
D4=119.999966

C 0
6-31G(d,p)
****
H 0
6-31G
****



"""
        mol = Molecule(["C", "H", "H", "H", "H"], self.coords)
        gen_basis = "C 0\n6-31G(d,p)\n****\nH 0\n6-31G\n****"
        gau = GaussianInput(mol, functional="B3LYP", gen_basis=gen_basis,
                            dieze_tag="#N", route_parameters={"Pseudo": "Read"},
                            title="Test")
        self.assertEqual(gau.to_string(cart_coords=False), gau_str)


class GaussianOutputTest(unittest.TestCase):
    # todo: Add unittest for PCM type output.

    def setUp(self):
        self.gauout = GaussianOutput(os.path.join(test_dir, "methane.log"))

    def test_props(self):
        gau = self.gauout
        self.assertEqual(len(gau.energies), 3)
        self.assertAlmostEqual(gau.energies[-1], -39.9768775602)
        self.assertEqual(len(gau.structures), 4)
        for mol in gau.structures:
            self.assertEqual(mol.formula, 'H4 C1')
        self.assertIn("opt", gau.route)
        self.assertEqual("Minimum", gau.stationary_type)
        self.assertEqual("hf", gau.functional)
        self.assertEqual("3-21G", gau.basis_set)
        self.assertEqual(17, gau.num_basis_func)
        d = gau.as_dict()
        self.assertEqual(d["input"]["functional"], "hf")
        self.assertAlmostEqual(d["output"]["final_energy"], -39.9768775602)
        self.assertEqual(len(gau.cart_forces), 3)
        self.assertEqual(gau.cart_forces[0][ 5],  0.009791094)
        self.assertEqual(gau.cart_forces[0][-1], -0.003263698)
        self.assertEqual(gau.cart_forces[2][-1], -0.000000032)
<<<<<<< HEAD
=======
        self.assertEqual(gau.eigenvalues[Spin.up][-1], 1.95586)
        self.assertEqual(gau.num_basis_func, 17)
        self.assertEqual(gau.is_spin, False)
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b

        ch2o_co2 = GaussianOutput(os.path.join(test_dir, "CH2O_CO2.log"))
        self.assertEqual(len(ch2o_co2.frequencies), 2)
        self.assertEqual(ch2o_co2.frequencies[0][0][0], 1203.1940)
        self.assertListEqual(ch2o_co2.frequencies[0][1][1], [ 0.15, 0.00, 0.00,
                                                             -0.26, 0.65, 0.00,
                                                             -0.26,-0.65, 0.00,
                                                             -0.08, 0.00, 0.00])
        self.assertListEqual(ch2o_co2.frequencies[1][3][1], [ 0.00, 0.00, 0.88,
                                                              0.00, 0.00,-0.33,
                                                              0.00, 0.00,-0.33])
<<<<<<< HEAD
        
=======
        self.assertEqual(ch2o_co2.eigenvalues[Spin.up][3], -1.18394)

    def test_pop(self):
        gau = GaussianOutput(os.path.join(test_dir, "H2O_gau.out"))
        self.assertEqual(gau.num_basis_func, 13)
        self.assertEqual(gau.electrons, (5, 5))
        self.assertEqual(gau.is_spin, True)
        self.assertListEqual(gau.eigenvalues[Spin.down], [-20.55343,  -1.35264,
                                                           -0.72655,  -0.54824,
                                                           -0.49831,   0.20705,
                                                            0.30297,   1.10569,
                                                            1.16144,   1.16717,
                                                            1.20460,   1.38903,
                                                            1.67608])
        mo = gau.molecular_orbital
        self.assertEqual(len(mo), 2) # la 6
        self.assertEqual(len(mo[Spin.down]), 13)
        self.assertEqual(len(mo[Spin.down][0]), 3)
        self.assertEqual(mo[Spin.down][5][0]["1S"], -0.08771)
        self.assertEqual(mo[Spin.down][5][0]["2PZ"], -0.21625)
        self.assertListEqual(gau.eigenvectors[Spin.up][:, 5].tolist(), [-0.08771,
                                                                         0.10840,
                                                                         0.00000,
                                                                         0.00000,
                                                                        -0.21625,
                                                                         1.21165,
                                                                         0.00000,
                                                                         0.00000,
                                                                        -0.44481,
                                                                        -0.06348,
                                                                        -1.00532,
                                                                        -0.06348,
                                                                        -1.00532])

        self.assertListEqual(gau.atom_basis_labels[0], ["1S", "2S", "2PX", "2PY",
                                                        "2PZ", "3S", "3PX", "3PY",
                                                        "3PZ"])
        self.assertListEqual(gau.atom_basis_labels[2], ["1S", "2S"])

>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b
    def test_scan(self):
        gau = GaussianOutput(os.path.join(test_dir, "so2_scan.log"))
        d = gau.read_scan()
        self.assertAlmostEqual(-548.02102, d["energies"][-1])
        self.assertEqual(len(d["coords"]), 1)
        self.assertEqual(len(d["energies"]), len(gau.energies))
        self.assertEqual(len(d["energies"]), 21)
<<<<<<< HEAD
    
=======

>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b
    def test_td(self):
        gau = GaussianOutput(os.path.join(test_dir, "so2_td.log"))
        transitions = gau.read_excitation_energies()
        self.assertEqual(len(transitions), 4)
        self.assertAlmostEqual(transitions[0], (3.9281, 315.64, 0.0054))

if __name__ == "__main__":
    unittest.main()
