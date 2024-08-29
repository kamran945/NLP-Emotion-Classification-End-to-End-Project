from pathlib import Path

from src.emotionClassification.constants import *
from src.emotionClassification.utils.common import read_yaml_file, create_directories
from src.emotionClassification.entity import DataIngestionConfig


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
