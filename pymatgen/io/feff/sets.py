# coding: utf-8
# Copyright (c) Pymatgen Development Team.
# Distributed under the terms of the MIT License.

from __future__ import division, unicode_literals

"""
This module defines the FeffInputSet abstract base class and a concrete
implementation for the Materials Project.  The basic concept behind an input
set is to specify a scheme to generate a consistent set of Feff inputs from a
structure without further user intervention. This ensures comparability across
runs.
"""

<<<<<<< HEAD
import six

__author__ = "Alan Dozier"
__credits__ = "Anubhav Jain, Shyue Ping Ong"
__copyright__ = "Copyright 2011, The Materials Project"
__version__ = "1.0.3"
__maintainer__ = "Alan Dozier"
__email__ = "adozier@uky.edu"
__date__ = "April 7, 2013"

import os
import abc

from monty.serialization import loadfn

from pymatgen.io.feff import FeffAtoms, FeffTags, FeffPot, Header


class AbstractFeffInputSet(six.with_metaclass(abc.ABCMeta, object)):
    """
    Abstract base class representing a set of Feff input parameters.
    The idea is that using a FeffInputSet, a complete set of input files
    (feffPOT,feffXANES, feffEXAFS, ATOMS, feff.inp)set_
=======
import sys
import os
import abc
import six
from copy import deepcopy
import logging

from monty.serialization import loadfn
from monty.json import MSONable

from pymatgen.io.feff.inputs import Atoms, Tags, Potential, Header


__author__ = "Kiran Mathew"
__credits__ = "Alan Dozier, Anubhav Jain, Shyue Ping Ong"
__version__ = "1.1"
__maintainer__ = "Kiran Mathew"
__email__ = "kmathew@lbl.gov"
__date__ = "Sept 10, 2016"


MODULE_DIR = os.path.dirname(os.path.abspath(__file__))

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')
sh = logging.StreamHandler(stream=sys.stdout)
sh.setFormatter(formatter)
logger.addHandler(sh)


class AbstractFeffInputSet(six.with_metaclass(abc.ABCMeta, MSONable)):
    """
    Abstract base class representing a set of Feff input parameters.
    The idea is that using a FeffInputSet, a complete set of input files
    (feffPOT, feffXANES, feffEXAFS, ATOMS, feff.inp)set_
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b
    can be generated in an automated fashion for any structure.
    """

    @abc.abstractmethod
<<<<<<< HEAD
    def get_feff_atoms(self, structure, central_atom):
        """
        Returns Atoms string from a structure that goes in feff.inp file.

        Args:
            structure: pymatgen structure object
            central_atom: atom symbol string for absorbing atom

        Returns:
            FeffAtoms object.
        """
        return

    @abc.abstractmethod
    def get_feff_tags(self, calc_type):
        """
        Returns standard calculation paramters for either an FEFF XANES or
        EXAFS input.

        Args:
            calc_type: At this time either 'XANES' or 'EXAFS' string is
                supported for K shell excitation. In the future this will be
                expanded to include other shells and material class
                differentiation.
        """
        return

    @abc.abstractmethod
    def get_feff_pot(self, structure, central_atom):
        """
        Returns POTENTIAL section used in feff.inp from a structure.

        Args:
            structure: pymatgen structure object
            central_atom: atom symbol string for absorbing atom
        """
        return

    @abc.abstractmethod
    def get_header(self, structure, source, comment):
        """
        Returns header to be used in feff.inp file from a pymatgen structure

        Args:
            structure: A pymatgen structure object
            source: Source identifier used to create structure, can be defined
                however user wants to organize structures, calculations, etc.
                example would be Materials Project material ID number.
        """
        return

    def get_all_feff_input(self, structure, calc_type, source, central_atom,
                           comment=''):
        """
        Returns all input files as a dict of {filename: feffio object}

        Args:
            structure: Structure object
            calc_type: At this time either 'XANES' or 'EXAFS' string is
                supported for K shell excitation. In the future this will be
                expanded to inlude other shells and material class
                differentiation.
            source: Source identifier used to create structure, can be defined
                however user wants to organize structures, calculations, etc.
                example would be Materials Project material ID number.
            central_atom: Atom symbol string for absorbing atom
            comment: Comment to appear in Header.

        Returns:
            dict of objects used to create feff.inp file i.e. Header, FeffTags,
            FeffPot, FeffAtoms
        """

        feff = {"HEADER": self.get_header(structure, source, comment),
                "PARAMETERS": self.get_feff_tags(calc_type),
                "POTENTIALS": self.get_feff_pot(structure, central_atom),
                "ATOMS": self.get_feff_atoms(structure, central_atom)}

        return feff

    def write_input(self, structure, calc_type, source, central_atom,
                    comment='', output_dir=".", make_dir_if_not_present=True):
=======
    def header(self):
        """
        Returns header to be used in feff.inp file from a pymatgen structure
        """
        pass

    @abc.abstractproperty
    def atoms(self):
        """
        Returns Atoms string from a structure that goes in feff.inp file.

        Returns:
            Atoms object.
        """
        pass

    @abc.abstractproperty
    def tags(self):
        """
        Returns standard calculation parameters.
        """
        return

    @abc.abstractproperty
    def potential(self):
        """
        Returns POTENTIAL section used in feff.inp from a structure.
        """
        pass

    def all_input(self):
        """
        Returns all input files as a dict of {filename: feffio object}
        """
        d = {"HEADER": self.header(), "PARAMETERS": self.tags}

        if "RECIPROCAL" not in self.tags:
            d.update({"POTENTIALS": self.potential, "ATOMS": self.atoms})

        return d

    def write_input(self, output_dir=".", make_dir_if_not_present=True):
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b
        """
        Writes a set of FEFF input to a directory.

        Args:
<<<<<<< HEAD
            structure: Structure object
            calc_type: At this time either 'XANES' or 'EXAFS' string is
                supported for K shell excitation. In the future this will be
                expanded to include other shells and material class
                differentiation.
            source: Source identifier used to create structure, can be defined
                however user wants to organize structures, calculations, etc.
                example would be Materials Project material ID number.
            central_atom: Atom symbol string for absorbing atom
            output_dir: Directory to output the FEFF input files
            comment: comment for Header
            make_dir_if_not_present: Set to True if you want the directory (
                and the whole path) to be created if it is not present.
        """

        if make_dir_if_not_present and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        feff = self.get_all_feff_input(structure, calc_type, source,
                                       central_atom, comment)

        feff_input = "\n\n".join(str(feff[f]) for f in ["HEADER", "PARAMETERS",
                                 "POTENTIALS", "ATOMS"])
=======
            output_dir: Directory to output the FEFF input files
            make_dir_if_not_present: Set to True if you want the directory (
                and the whole path) to be created if it is not present.
        """
        if make_dir_if_not_present and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        feff = self.all_input()

        feff_input = "\n\n".join(str(feff[k]) for k in
                                 ["HEADER", "PARAMETERS", "POTENTIALS", "ATOMS"]
                                 if k in feff)
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b

        for k, v in six.iteritems(feff):
            with open(os.path.join(output_dir, k), "w") as f:
                f.write(str(v))

        with open(os.path.join(output_dir, "feff.inp"), "w") as f:
            f.write(feff_input)
<<<<<<< HEAD
        f.close()

    def as_dict(self, structure, calc_type, source, central_atom,
                comment=''):
        """Creates a feff.inp dictionary as a string"""

        feff = self.get_all_feff_input(structure, calc_type, source,
                                       central_atom, comment)
        feff_input = "\n\n".join(str(feff[f]) for f in ["HEADER", "PARAMETERS",
                                 "POTENTIALS", "ATOMS"])
        return {'@module': self.__class__.__module__,
                '@class': self.__class__.__name__,
                'feff.inp': feff_input}

    @staticmethod
    def from_dict(d):
        """Return feff.inp from a dictionary string representation"""
        return d['feff.inp']


class FeffInputSet(AbstractFeffInputSet):
    """
    Standard implementation of FeffInputSet, which can be extended by specific
    implementations.

    Args:
        name: The name of a grouping of input parameter sets such as
            "MaterialsProject".
    """

    def __init__(self, name):
        self.name = name
        module_dir = os.path.dirname(os.path.abspath(__file__))
        config = loadfn(os.path.join(module_dir, "FeffInputSets.yaml"))
        self.xanes_settings = config[self.name + "feffXANES"]
        self.exafs_settings = config[self.name + "feffEXAFS"]

    def get_header(self, structure, source='', comment=''):
=======

        # write the structure to cif file
        if "ATOMS" not in feff:
            self.atoms.struct.to(fmt="cif",
                                 filename=os.path.join(
                                     output_dir, feff["PARAMETERS"]["CIF"]))


class FEFFDictSet(AbstractFeffInputSet):
    """
    Standard implementation of FeffInputSet, which can be extended by specific
    implementations.
    """

    def __init__(self, absorbing_atom, structure, radius, config_dict,
                 edge="K", spectrum="EXAFS", nkpts=1000, user_tag_settings=None):
        """

        Args:
            absorbing_atom (str/int): absorbing atom symbol or site index
            structure (Structure): input structure
            radius (float): cluster radius
            config_dict (dict): control tag settings dict
            edge (str): absorption edge
            spectrum (str): type of spectrum to calculate, available options :
                EXAFS, XANES, DANES, XMCD, ELNES, EXELFS, FPRIME, NRIXS, XES.
                The default is EXAFS.
            nkpts (int): Total number of kpoints in the brillouin zone. Used
                only when feff is run in the reciprocal space mode.
            user_tag_settings (dict): override default tag settings. To delete
                tags, set the key '_del' in the user_tag_settings.
                eg: user_tag_settings={"_del": ["COREHOLE", "EXCHANGE"]}
        """
        self.absorbing_atom = absorbing_atom
        self.structure = structure
        self.radius = radius
        self.config_dict = deepcopy(config_dict)
        self.edge = edge
        self.spectrum = spectrum
        self.nkpts = nkpts
        self.user_tag_settings = user_tag_settings or {}
        self.config_dict["EDGE"] = self.edge
        self.config_dict.update(self.user_tag_settings)
        if "_del" in self.user_tag_settings:
            for tag in self.user_tag_settings["_del"]:
                if tag in self.config_dict:
                    del self.config_dict[tag]
            del self.config_dict["_del"]
        # k-space feff only for small systems. The hardcoded system size in
        # feff is around 14 atoms.
        self.small_system = True if len(self.structure) < 14 else False

    def header(self, source='', comment=''):
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b
        """
        Creates header string from structure object

        Args:
<<<<<<< HEAD
            structure: A pymatgen structure object
=======
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b
            source: Source identifier used to create structure, can be defined
                however user wants to organize structures, calculations, etc.
                example would be Materials Project material ID number.
            comment: comment to include in header

        Returns:
<<<<<<< HEAD
            Header object to be used in feff.inp file from a pymatgen structure
        """
        return Header(structure, source, comment)

    def get_feff_tags(self, calc_type):
        """
        Reads standard parameters for XANES or EXAFS calculation
        from FeffInputSets.yaml file.

        Args:
            calc_type: At this time either 'XANES' or 'EXAFS' string is
                supported for K shell excitation. In the future this will be
                expanded to include other shells and material class
                differentiation.

        Returns:
            FeffTags object
        """

        if calc_type.upper() == "XANES":
            fefftags = FeffTags(self.xanes_settings)
        elif calc_type.upper() == "EXAFS":
            fefftags = FeffTags(self.exafs_settings)
        else:
            raise ValueError("{} is not a valid calculation type"
                             .format(calc_type))

        return fefftags

    def get_feff_pot(self, structure, central_atom):
        """
        Creates string representation of potentials used in POTENTIAL file and
        feff.inp.

        Args:
            structure: pymatgen structure object
            central_atom: atom symbol string for absorbing atom

        Returns:
            FeffPot object
        """
        return FeffPot(structure, central_atom)

    def get_feff_atoms(self, structure, central_atom):
        """
        Creates string representation of atomic shell coordinates using in
        ATOMS file and feff.inp.

        Args:
            structure: pymatgen structure object
            central_atom: atom symbol string for absorbing atom

        Returns:
            FeffAtoms object
        """
        return FeffAtoms(structure, central_atom)

    def __str__(self):
        output = [self.name]
        section_names = ["XANES", "EXAFS"]
        for ns in section_names:
            for d in [self.xanes_settings, self.exafs_settings]:
                output.append(ns)
                for k, v in six.iteritems(d):
                    output.append("%s = %s" % (k, str(v)))
                output.append("")

        return "\n".join(output)


class MaterialsProjectFeffInputSet(FeffInputSet):
    """
    Implementation of FeffInputSet utilizing parameters in the public
    Materials Project.
    """
    def __init__(self):
        super(MaterialsProjectFeffInputSet, self).__init__("MaterialsProject")
=======
            Header
        """
        return Header(self.structure, source, comment)

    @property
    def tags(self):
        """
        FEFF job parameters.

        Returns:
            Tags
        """
        if "RECIPROCAL" in self.config_dict:
            if self.small_system:
                self.config_dict["CIF"] = "{}.cif".format(
                    self.structure.formula.replace(" ", ""))
                self.config_dict["TARGET"] = self.atoms.center_index + 1
                self.config_dict["COREHOLE"] = "RPA"
                logger.warn("Setting COREHOLE = RPA for K-space calculation")
                if not self.config_dict.get("KMESH", None):
                    abc = self.structure.lattice.abc
                    mult = (self.nkpts * abc[0] * abc[1] * abc[2]) ** (1 / 3)
                    self.config_dict["KMESH"] = [int(round(mult / l)) for l in abc]
            else:
                logger.warn("Large system(>=14 atoms), removing K-space settings")
                del self.config_dict["RECIPROCAL"]
                self.config_dict.pop("CIF", None)
                self.config_dict.pop("TARGET", None)
                self.config_dict.pop("KMESH", None)
                self.config_dict.pop("STRFAC", None)

        return Tags(self.config_dict)

    @property
    def potential(self):
        """
        FEFF potential

        Returns:
            Potential
        """
        return Potential(self.structure, self.absorbing_atom)

    @property
    def atoms(self):
        """
        absorber + the rest

        Returns:
            Atoms
        """
        return Atoms(self.structure, self.absorbing_atom, self.radius)

    def __str__(self):
        output = [self.spectrum]
        output.extend(["%s = %s" % (k, str(v))
                       for k, v in six.iteritems(self.config_dict)])
        output.append("")
        return "\n".join(output)


class MPXANESSet(FEFFDictSet):
    """
    FeffDictSet for XANES spectroscopy.
    """

    CONFIG = loadfn(os.path.join(MODULE_DIR, "MPXANESSet.yaml"))

    def __init__(self, absorbing_atom, structure, edge="K", radius=10.,
                 nkpts=1000, **kwargs):
        """
        Args:
            absorbing_atom (str/int): absorbing atom symbol or site index
            structure (Structure): input
            edge (str): absorption edge
            radius (float): cluster radius in Angstroms.
            nkpts (int): Total number of kpoints in the brillouin zone. Used
                only when feff is run in the reciprocal space mode.
            **kwargs
        """
        super(MPXANESSet, self).__init__(absorbing_atom, structure, radius,
                                         MPXANESSet.CONFIG, edge=edge,
                                         spectrum="XANES", nkpts=nkpts, **kwargs)
        self.kwargs = kwargs


class MPEXAFSSet(FEFFDictSet):
    """
    FeffDictSet for EXAFS spectroscopy.
    """

    CONFIG = loadfn(os.path.join(MODULE_DIR, "MPEXAFSSet.yaml"))

    def __init__(self, absorbing_atom, structure, edge="K", radius=10.,
                 nkpts=1000, **kwargs):
        """
        Args:
            absorbing_atom (str/int): absorbing atom symbol or site index
            structure (Structure): input structure
            edge (str): absorption edge
            radius (float): cluster radius in Angstroms.
            nkpts (int): Total number of kpoints in the brillouin zone. Used
                only when feff is run in the reciprocal space mode.
            **kwargs
        """
        super(MPEXAFSSet, self).__init__(absorbing_atom, structure, radius,
                                         MPEXAFSSet.CONFIG, edge=edge,
                                         spectrum="EXAFS", nkpts=nkpts, **kwargs)
        self.kwargs = kwargs


class MPEELSDictSet(FEFFDictSet):
    """
    FeffDictSet for ELNES spectroscopy.
    """

    def __init__(self, absorbing_atom, structure, edge, spectrum, radius,
                 beam_energy, beam_direction, collection_angle,
                 convergence_angle, config_dict, user_eels_settings=None,
                 nkpts=1000, **kwargs):
        """
        Args:
            absorbing_atom (str/int): absorbing atom symbol or site index
            structure (Structure): input structure
            edge (str): absorption edge
            spectrum (str): ELNES or EXELFS
            radius (float): cluster radius in Angstroms.
            beam_energy (float): Incident beam energy in keV
            beam_direction (list): Incident beam direction. If None, the
                cross section will be averaged.
            collection_angle (float): Detector collection angle in mrad.
            convergence_angle (float): Beam convergence angle in mrad.
            user_eels_settings (dict): override default EELS config.
                See MPELNESSet.yaml for supported keys.
            nkpts (int): Total number of kpoints in the brillouin zone. Used
                only when feff is run in the reciprocal space mode.
            **kwargs
        """
        self.beam_energy = beam_energy
        self.beam_direction = beam_direction
        self.collection_angle = collection_angle
        self.convergence_angle = convergence_angle
        self.user_eels_settings = user_eels_settings
        eels_config_dict = deepcopy(config_dict)

        if beam_direction:
            beam_energy_list = [beam_energy, 0, 1, 1]
            eels_config_dict[spectrum]["BEAM_DIRECTION"] = beam_direction
        else:
            beam_energy_list = [beam_energy, 1, 0, 1]
            del eels_config_dict[spectrum]["BEAM_DIRECTION"]
        eels_config_dict[spectrum]["BEAM_ENERGY"] = beam_energy_list
        eels_config_dict[spectrum]["ANGLES"] = [collection_angle,
                                                convergence_angle]

        if user_eels_settings:
            eels_config_dict[spectrum].update(user_eels_settings)

        super(MPEELSDictSet, self).__init__(absorbing_atom, structure, radius,
                                            eels_config_dict, edge=edge,
                                            spectrum=spectrum, nkpts=nkpts,
                                            **kwargs)
        self.kwargs = kwargs


class MPELNESSet(MPEELSDictSet):
    """
    FeffDictSet for ELNES spectroscopy.
    """

    CONFIG = loadfn(os.path.join(MODULE_DIR, "MPELNESSet.yaml"))

    def __init__(self, absorbing_atom, structure, edge="K", radius=10.,
                 beam_energy=100, beam_direction=None, collection_angle=1,
                 convergence_angle=1, user_eels_settings=None, nkpts=1000,
                 **kwargs):
        """
        Args:
            absorbing_atom (str/int): absorbing atom symbol or site index
            structure (Structure): input structure
            edge (str): absorption edge
            radius (float): cluster radius in Angstroms.
            beam_energy (float): Incident beam energy in keV
            beam_direction (list): Incident beam direction. If None, the
                cross section will be averaged.
            collection_angle (float): Detector collection angle in mrad.
            convergence_angle (float): Beam convergence angle in mrad.
            user_eels_settings (dict): override default EELS config.
                See MPELNESSet.yaml for supported keys.
            nkpts (int): Total number of kpoints in the brillouin zone. Used
                only when feff is run in the reciprocal space mode.
            **kwargs
        """

        super(MPELNESSet, self).__init__(absorbing_atom, structure, edge,
                                         "ELNES", radius, beam_energy,
                                         beam_direction, collection_angle,
                                         convergence_angle, MPELNESSet.CONFIG,
                                         user_eels_settings=user_eels_settings,
                                         nkpts=nkpts, **kwargs)
        self.kwargs = kwargs


class MPEXELFSSet(MPEELSDictSet):
    """
    FeffDictSet for EXELFS spectroscopy.
    """

    CONFIG = loadfn(os.path.join(MODULE_DIR, "MPEXELFSSet.yaml"))

    def __init__(self, absorbing_atom, structure, edge="K", radius=10.,
                 beam_energy=100, beam_direction=None, collection_angle=1,
                 convergence_angle=1, user_eels_settings=None, nkpts=1000,
                 **kwargs):
        """
        Args:
            absorbing_atom (str/int): absorbing atom symbol or site index
            structure (Structure): input structure
            edge (str): absorption edge
            radius (float): cluster radius in Angstroms.
            beam_energy (float): Incident beam energy in keV
            beam_direction (list): Incident beam direction. If None, the
                cross section will be averaged.
            collection_angle (float): Detector collection angle in mrad.
            convergence_angle (float): Beam convergence angle in mrad.
            user_eels_settings (dict): override default EELS config.
                See MPEXELFSSet.yaml for supported keys.
            nkpts (int): Total number of kpoints in the brillouin zone. Used
                only when feff is run in the reciprocal space mode.
            **kwargs
        """

        super(MPEXELFSSet, self).__init__(absorbing_atom, structure, edge,
                                          "EXELFS", radius, beam_energy,
                                          beam_direction, collection_angle,
                                          convergence_angle, MPEXELFSSet.CONFIG,
                                          user_eels_settings=user_eels_settings,
                                          nkpts=nkpts, **kwargs)
        self.kwargs = kwargs
>>>>>>> a41cc069c865a5d0f35d0731f92c547467395b1b
