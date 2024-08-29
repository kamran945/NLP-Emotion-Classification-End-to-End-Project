import os

from datasets import load_dataset

from src.emotionClassification.entity import DataIngestionConfig
from src.emotionClassification.logging import logger
from src.emotionClassification.utils.common import get_directory_size


class DataIngestion:
    """
    Represents a data ingestion process.
    """

    def __init__(self, config: DataIngestionConfig) -> None:
        """
        Initialize the DataIngestion class with the given configuration.
        """
        self.config = config

    def download_data(self) -> None:
        """
        Download the data specified in the configuration.
        """
        print(f"Downloading data from {self.config.source_url}")

        local_file = self.config.local_data_file
        print(f"Size of {local_file} is {os.path.getsize(local_file)}")
        if get_directory_size(local_file) == 0:

            ds = load_dataset(
                self.config.source_url, "subtask5.english", trust_remote_code=True
            )

            # Save the dataset to a local file
            ds.save_to_disk(local_file)

            print(f"File downloaded successfully as {local_file}")
            logger.info(f"Downloaded {local_file}")
        else:
            logger.info(
                f"Data file {local_file} already exists with size {get_directory_size(local_file)}"
            )
