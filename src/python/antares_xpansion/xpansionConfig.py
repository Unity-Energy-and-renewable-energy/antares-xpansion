"""
    parameters for an AntaresXpansion session
"""
from dataclasses import dataclass
from pathlib import Path
import os
import sys
import yaml
from typing import List




@dataclass
class ConfigParameters:
    ANTARES: str
    MERGE_MPS: str
    BENDERS_MPI: str
    BENDERS_SEQUENTIAL: str
    LP_NAMER: str
    STUDY_UPDATER: str
    AVAILABLE_SOLVERS: List[str]

@dataclass
class InputParameters:
    step: str
    simulation_name: str
    data_dir: str
    install_dir: str
    method: str
    n_mpi: int
    antares_n_cpu : int
    keep_mps: bool


class XpansionConfig:
    """
        Class defininf the parameters for an AntaresXpansion session
    """

    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-few-public-methods

    def __init__(self, input_parameters: InputParameters, config_parameters: ConfigParameters):

        self.input_parameters = input_parameters
        self.config_parameters = config_parameters
        self.ANTARES: str = ""
        self.MERGE_MPS: str = ""
        self.BENDERS_MPI: str = ""
        self.BENDERS_SEQUENTIAL: str = ""
        self.LP_NAMER: str = ""
        self.STUDY_UPDATER: str = ""
        self.MPI_LAUNCHER: str = ""
        self.MPI_N: str = ""
        self.AVAILABLE_SOLVER: List[str]

        self._get_config_values()

        self._get_parameters_from_arguments()

        self._initialize_default_values()

    def _get_parameters_from_arguments(self):
        self.step = self.input_parameters.step
        self.simulation_name = self.input_parameters.simulation_name
        self.data_dir = str(Path(self.input_parameters.data_dir).absolute())
        self.install_dir = self._get_install_dir(self.input_parameters.install_dir)
        self.method = self.input_parameters.method
        self.n_mpi = self.input_parameters.n_mpi
        self.antares_n_cpu = self.input_parameters.antares_n_cpu
        self.keep_mps = self.input_parameters.keep_mps

    def _get_install_dir(self, install_dir):
        if install_dir is None:
            return self._initialize_install_dir_with_default_value()
        else:
            return self._initialize_install_dir_with_absolute_path(install_dir)

    @staticmethod
    def _initialize_install_dir_with_absolute_path(install_dir):
        if not Path.is_absolute(Path(install_dir)):
            return os.path.join(Path.cwd(), Path(install_dir))
        else:
            return install_dir

    @staticmethod
    def _initialize_install_dir_with_default_value():
        install_dir_inside_package = Path(os.path.abspath(__file__)).parent.parent / "bin"
        install_dir_from_absolute_path = Path.cwd() / "bin"
        if Path.is_dir(install_dir_inside_package):
            return install_dir_inside_package
        else:
            return install_dir_from_absolute_path

    def _initialize_default_values(self):
        self._set_constants()
        self._set_default_options()
        self._set_default_settings()

    def _set_constants(self):
        #TODO move self.SETTINGS, self.GENERAL_DATA_INI, self.OUTPUT into antares driver
        self.SETTINGS = 'settings' 
        self.GENERAL_DATA_INI = 'generaldata.ini'
        self.OUTPUT = 'output'

        self.USER = 'user'
        self.EXPANSION = 'expansion'
        self.CAPADIR = 'capa'
        self.NB_YEARS = 'nbyears'
        self.SETTINGS_INI = 'settings.ini'
        self.CANDIDATES_INI = 'candidates.ini'
        self.UC_TYPE = 'uc_type'
        self.EXPANSION_ACCURATE = 'expansion_accurate'
        self.EXPANSION_FAST = 'expansion_fast'
        self.OPTIONS_TXT = 'options.txt'

    def _set_default_settings(self):
        self.settings_default = {
            "method": "benders_decomposition",
            "uc_type": "expansion_fast",
            "master": "integer",
            "optimality_gap": "1",
            "relative_gap": "1e-12",
            "cut_type": "yearly",
            "week_selection": "false",
            "max_iteration": "+infini",
            "relaxed_optimality_gap": "0.01",
            "solver": "Cbc",
            "timelimit": "+infini",
            "additional-constraints": "",
            "yearly-weights": "",
        }

    def _set_default_options(self):
        self.options_default = {
            "LOG_LEVEL": "0",
            "MAX_ITERATIONS": "-1",
            "ABSOLUTE_GAP": "1",
            "RELATIVE_GAP": "1e-12",
            "AGGREGATION": "0",
            "OUTPUTROOT": ".",
            "TRACE": "1",
            "DELETE_CUT": "0",
            "SLAVE_WEIGHT": "CONSTANT",
            "SLAVE_WEIGHT_VALUE": "1",
            "MASTER_NAME": "master",
            "SLAVE_NUMBER": "-1",
            "STRUCTURE_FILE": "structure.txt",
            "INPUTROOT": ".",
            "BASIS": "1",
            "ACTIVECUTS": "0",
            "THRESHOLD_AGGREGATION": "0",
            "THRESHOLD_ITERATION": "0",
            "RAND_AGGREGATION": "0",
            "CSV_NAME": "benders_output_trace",
            "JSON_NAME": "out",
            "BOUND_ALPHA": "1",
        }


    def _get_config_values(self):
        
        self.ANTARES = self.config_parameters.ANTARES
        self.MERGE_MPS = self.config_parameters.MERGE_MPS
        self.BENDERS_MPI = self.config_parameters.BENDERS_MPI
        self.BENDERS_SEQUENTIAL = self.config_parameters.BENDERS_SEQUENTIAL
        self.LP_NAMER = self.config_parameters.LP_NAMER
        self.STUDY_UPDATER = self.config_parameters.STUDY_UPDATER
        self.AVAILABLE_SOLVER = self.config_parameters.AVAILABLE_SOLVERS
    
