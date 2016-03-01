# coding: utf-8
# Copyright (c) Pymatgen Development Team.
# Distributed under the terms of the MIT License.

from __future__ import division, unicode_literals

"""
TODO: Modify unittest doc.
"""

__author__ = "Shyam Dwaraknath"
__copyright__ = "Copyright 2016, The Materials Project"
__version__ = "0.1"
__maintainer__ = "Shyam Dwaraknath"
__email__ = "shyamd@lbl.gov"
__date__ = "2/5/16"

import unittest
from pymatgen.core.lattice import Lattice
from pymatgen.core.structure import Structure
from pymatgen.analysis.interfaces.topology import ZSLGenerator as ZSLGen
from pymatgen.util.testing import PymatgenTest
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.matproj.rest import MPRester


class ZSLGenTest(PymatgenTest):

    def runTest(self):
        mprest = MPRester()

        #Film VO2
        structure_import = mprest.get_structure_by_material_id('mp-19094',final=True)
        film = SpacegroupAnalyzer(structure_import,symprec=0.1).get_conventional_standard_structure()

        #Substrate
        structure_import = mprest.get_structure_by_material_id('mp-554278',final=True)
        substrate = SpacegroupAnalyzer(structure_import,symprec=0.1).get_conventional_standard_structure()

        z = ZSLGen(film,substrate)


        self.assertArrayEqual(z.reduce_vectors([1,0,0],[2,2,0]),[[1,0,0],[0,2,0]])
        self.assertEqual(z.area([1,0,0],[0,2,0]),2)
        self.assertArrayEqual(list(z.factor(18)),[1,2,3,6,9,18])
        self.assertTrue(z.is_same_vectors([[1.01,0,0],[0,2,0]],[[1,0,0],[0,2.01,0]]))
        self.assertFalse(z.is_same_vectors([[1.01,2,0],[0,2,0]],[[1,0,0],[0,2.01,0]]))

        matches = list(z.generate())
        for m in matches:
            print str(m.as_dict())

        self.assertEqual(len(matches),82)

        # TODO: Add in test for vector angle calculate
        # TODO: Add in test for checking if two sets of vectors are equivelant
        # TODO: Add in test for checking transformations

if __name__ == '__main__':
    unittest.main()
    #z = ZSLGenTest()
    #z.runTest()
