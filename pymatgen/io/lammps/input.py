# coding: utf-8
# Copyright (c) Pymatgen Development Team.
# Distributed under the terms of the MIT License.

<<<<<<< HEAD
from __future__ import division, print_function, unicode_literals, \
    absolute_import

"""
This module implements classes for generating Lammps input files.
The input files consist of the main input file with the control parameters and
the data file.
"""

import json
=======
from __future__ import division, print_function, unicode_literals, absolute_import

"""
This module implements classes for generating Lammps input.

For the ease of management we divide LAMMPS input into 2 files:

    1.Data file: All structure related settings such as the atomic positions,
            bonds, angles, dihedrals, corresponding parametrizations etc are
            set in the data file.

    2. Control file: This is the main input file that should be fed to the
            lammps binary. The main input file consists of the path to the
            afore-mentioned data file and the job control parameters such as
            the ensemble type(NVT, NPT etc), max number of iterations etc.
"""

import six
import json   
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b
import os
from functools import partial
from collections import OrderedDict

from monty.json import MSONable, MontyDecoder

from pymatgen.io.lammps.data import LammpsData, LammpsForceFieldData

__author__ = "Kiran Mathew"
<<<<<<< HEAD
__credits__ = "Navnidhi Rajput"
__email__ = "kmathew@lbl.gov"
=======
__email__ = "kmathew@lbl.gov"
__credits__ = "Navnidhi Rajput"
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))


class DictLammpsInput(MSONable):
    """
    Implementation of LammpsInputSet that is initialized from a dict
    settings. It is typically used by other LammpsInputSets for
    initialization from json or yaml source files.

    Args:
        name (str): A name for the input set.
        config_dict (dict): The config dictionary to use.
        lammps_data (LammpsData): LammpsData object
        data_filename (str): name of the the lammps data file
        user_lammps_settings (dict): User lammps settings. This allows a user
            to override lammps settings, e.g., setting a different force field
            or bond type.
    """

    def __init__(self, name, config_dict, lammps_data=None,
<<<<<<< HEAD
                 data_file="in.data", user_lammps_settings={}):
=======
                 data_filename="in.data", user_lammps_settings={}):
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b
        self.name = name
        self.lines = []
        self.config_dict = config_dict
        self.lammps_data = lammps_data
<<<<<<< HEAD
        self.data_file = data_file
        self.config_dict["read_data"] = data_file
=======
        self.data_filename = data_filename
        self.config_dict["read_data"] = data_filename
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b
        self.user_lammps_settings = user_lammps_settings
        if self.user_lammps_settings:
            self.config_dict.update(self.user_lammps_settings)

    def __str__(self):
        """
        string representation of the lammps input file with the
        control parameters
        """
        lines = ""
        for k1, v1 in self.config_dict.items():
            if isinstance(v1, dict):
                v1 = v1.values()
            if isinstance(v1, list):
                for x in v1:
                    lines = "".join([lines, "{} ".format(k1)])
                    lines = "".join([lines, str(x), os.linesep])
            else:
                lines = "".join([lines, "{} ".format(k1)])
                lines = "".join([lines, " {}{}".format(str(v1), os.linesep)])
        return lines

<<<<<<< HEAD
    def write_input(self, filename, data_file=None):
        """
        get the string representation of the main input file and write it.
=======
    def write_input(self, filename, data_filename=None):
        """
        Get the string representation of the main input file and write it.
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b
        Also writes the data file if the lammps_data attribute is set.

        Args:
            filename (string): name of the input file
<<<<<<< HEAD
        """
        if data_file:
            self.config_dict["read_data"] = data_file
            self.data_file = data_file
=======
            data_filename (string): override the data file name with this
        """
        if data_filename:
            self.config_dict["read_data"] = data_filename
            self.data_filename = data_filename
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b
        # write the main input file
        with open(filename, 'w') as f:
            f.write(self.__str__())
        # write the data file if present
        if self.lammps_data:
<<<<<<< HEAD
            print("Writing the data to {}".format(self.data_file))
            self.lammps_data.write_data_file(filename=self.data_file)

    @staticmethod
    def from_file(name, filename, data_obj=None, data_file=None,
                  is_forcefield=False):
        """
        Read in the input settings from json file as ordereddict. Also
        reads in the datafile if provided.
=======
            print("Data file: {}".format(self.data_filename))
            self.lammps_data.write_data_file(filename=self.data_filename)

    @staticmethod
    def from_file(name, filename, lammps_data=None, data_filename="in.data",
                  user_lammps_settings={}, is_forcefield=False):
        """
        Read in the input settings from json file as ordereddict.
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b
        Note: with monty.serialization.loadfn the order of paramters in the
        json file is not preserved

        Args:
            filename (string): name of the file with the lamps control
                paramters
<<<<<<< HEAD
            data_obj (LammpsData): LammpsData object
            data_file (string): name of the data file name
            is_forcefield (bool): whether the data file has forcefield and
                topology info in it.
=======
            lammps_data (string/LammpsData/LammpsForceFieldData): path to the
                data file or an appropriate object
            data_filename (string): name of the the lammps data file
            user_lammps_settings (dict): User lammps settings
            is_forcefield (bool): whether the data file has forcefield and
                topology info in it. This is required only if lammps_data is
                a path to the data file instead of a data object
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b

        Returns:
            DictLammpsInput
        """
        with open(filename) as f:
            config_dict = json.load(f, object_pairs_hook=OrderedDict)
<<<<<<< HEAD
        lammps_data = None
        if data_file:
            if is_forcefield:
                lammps_data = LammpsForceFieldData.from_file(data_file)
            else:
                lammps_data = LammpsData.from_file(data_file)
        if data_obj and isinstance(data_obj, LammpsData):
            lammps_data = data_obj
        return DictLammpsInput(name, config_dict, lammps_data)
=======
        lammps_data = lammps_data
        if isinstance(lammps_data, six.string_types):
            if is_forcefield:
                lammps_data = LammpsForceFieldData.from_file(lammps_data)
            else:
                lammps_data = LammpsData.from_file(lammps_data)
        return DictLammpsInput(name, config_dict, lammps_data=lammps_data,
                               data_filename=data_filename,
                               user_lammps_settings=user_lammps_settings)
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b

    def as_dict(self):
        d = MSONable.as_dict(self)
        if hasattr(self, "kwargs"):
            d.update(**self.kwargs)
<<<<<<< HEAD
        d["config_dict"] = self.config_dict.items()
=======
        d["config_dict"] = list(self.config_dict.items())
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b
        return d

    @classmethod
    def from_dict(cls, d):
        decoded = {k: MontyDecoder().process_decoded(v) for k, v in d.items()
                   if k not in ["@module", "@class", "config_dict"]}
        decoded["config_dict"] = OrderedDict(d["config_dict"])
        return cls(**decoded)


# NVT
NVTLammpsInput = partial(DictLammpsInput.from_file, "NVT",
                         os.path.join(MODULE_DIR, "NVT.json"))

# NPT
NPTLammpsInput = partial(DictLammpsInput.from_file, "NPT",
                         os.path.join(MODULE_DIR, "NPT.json"))

# NPT followed by NVT
NPTNVTLammpsInput = partial(DictLammpsInput.from_file, "NPT_NVT",
                            os.path.join(MODULE_DIR, "NPT_NVT.json"))
