from pathlib import Path

from src.emotionClassification.constants import *
from src.emotionClassification.utils.common import read_yaml_file, create_directories
from src.emotionClassification.entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataCleaningConfig,
)


class ConfigurationManager:
    """
    Class to manage the configuration parameters and initialize configurations.
    """

    def __init__(
        self,
        config_file_path: Path = CONFIG_FILE_PATH,
        params_file_path: Path = PARAMS_FILE_PATH,
    ) -> None:
        """
        Initialize the ConfigurationManager with the provided file paths.
        """

        self.config = read_yaml_file(config_file_path)
        self.params = read_yaml_file(params_file_path)

        create_directories(filepath_list=[self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Return the DataIngestionConfig object initialized with the configuration parameters.
        """
        config = self.config.data_ingestion

        create_directories([config.root_dir, config.local_data_file])

        return DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            extract_dir=config.extract_dir,
        )

    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Return the DataValidationConfig object initialized with the configuration parameters.
        """
        config = self.config.data_validation

        create_directories([config.root_dir])

        return DataValidationConfig(
            root_dir=config.root_dir,
            data_ingestion_dir=config.data_ingestion_dir,
            STATUS_FILE=config.STATUS_FILE,
            REQUIRED_FILES=config.REQUIRED_FILES,
        )

    def get_data_cleaning_config_and_params(self) -> DataCleaningConfig:
        """
        Return the DataCleaningConfig object initialized with the configuration parameters.
        """
        config = self.config.data_cleaning

        create_directories([config.root_dir, config.cleaned_dir])

        return (
            DataCleaningConfig(
                root_dir=config.root_dir,
                data_ingestion_dir=config.data_ingestion_dir,
                cleaned_dir=config.cleaned_dir,
            ),
            self.params.data_cleaning,
        )
