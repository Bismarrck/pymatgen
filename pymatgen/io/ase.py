# coding: utf-8
# Copyright (c) Pymatgen Development Team.
# Distributed under the terms of the MIT License.

from __future__ import division, unicode_literals, absolute_import

"""
This module provides conversion between the Atomic Simulation Environment
Atoms object and pymatgen Structure objects.
"""


__author__ = "Shyue Ping Ong"
__copyright__ = "Copyright 2012, The Materials Project"
__version__ = "1.0"
__maintainer__ = "Shyue Ping Ong"
__email__ = "shyuep@gmail.com"
__date__ = "Mar 8, 2012"

from pymatgen.core.structure import Structure

try:
    from ase import Atoms
    ase_loaded = True
except ImportError:
    ase_loaded = False


class AseAtomsAdaptor(object):
    """
    Adaptor serves as a bridge between ASE Atoms and pymatgen structure.
    """

    @staticmethod
    def get_atoms(structure):
        """
        Returns ASE Atoms object from pymatgen structure.

        Args:
            structure: pymatgen.core.structure.Structure

        Returns:
            ASE Atoms object
        """
        if not structure.is_ordered:
            raise ValueError("ASE Atoms only supports ordered structures")
        symbols = [str(site.specie.symbol) for site in structure]
        positions = [site.coords for site in structure]
        cell = structure.lattice.matrix
        return Atoms(symbols=symbols, positions=positions, pbc=True, cell=cell)

    @staticmethod
<<<<<<< HEAD
    def get_structure(atoms):
=======
    def get_structure(atoms, cls=None):
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b
        """
        Returns pymatgen structure from ASE Atoms.

        Args:
            atoms: ASE Atoms object
<<<<<<< HEAD
=======
            cls: The Structure class to instantiate (defaults to pymatgen structure)
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b

        Returns:
            Equivalent pymatgen.core.structure.Structure
        """
        symbols = atoms.get_chemical_symbols()
        positions = atoms.get_positions()
        lattice = atoms.get_cell()
<<<<<<< HEAD
        return Structure(lattice, symbols, positions,
                         coords_are_cartesian=True)
=======

        cls = Structure if cls is None else cls
        return cls(lattice, symbols, positions,
                   coords_are_cartesian=True)
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b
