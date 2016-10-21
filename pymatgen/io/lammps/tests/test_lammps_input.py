# coding: utf-8
<<<<<<< HEAD
=======
# Copyright (c) Pymatgen Development Team.
# Distributed under the terms of the MIT License.
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b

from __future__ import division, print_function, unicode_literals, \
    absolute_import

import os
import unittest

from pymatgen.io.lammps.input import DictLammpsInput

__author__ = 'Kiran Mathew'
__email__ = 'kmathew@lbl.gov'

test_dir = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..",
                        "test_files", "lammps")


class TestLammpsInput(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
<<<<<<< HEAD
        cls.lammps_input = DictLammpsInput.from_file("NVT",
                                                     os.path.join(test_dir,
                                                                  "NVT.json"),
                                                     data_file=os.path.join(
                                                         test_dir,
                                                         "nvt.data"),
                                                     is_forcefield=True)
=======
        cls.lammps_input = DictLammpsInput.from_file(
            "NVT", os.path.join(test_dir, "NVT.json"),
            data_filename=os.path.join(test_dir, "nvt.data"),
            is_forcefield=True)
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b

    def test_string_rep(self):
        self.lammps_input.config_dict["read_data"] = "nvt.data"
        with open(os.path.join(test_dir, "nvt.inp")) as f:
            self.assertEqual(str(self.lammps_input), "".join(f.readlines()))


if __name__ == "__main__":
    unittest.main()
