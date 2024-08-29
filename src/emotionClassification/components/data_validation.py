import os
from pathlib import Path

from src.emotionClassification.logging import logger
from src.emotionClassification.config.configuration import DataValidationConfig


class DataValidation:
    """
    Represents a data validation process.
    """

    def __init__(self, config: DataValidationConfig) -> None:
        """
        Initialize the DataValidation class with the given configuration.
        """
        self.config = config

    def validate_all_required_files_exist(self) -> bool:
        """
        Validate that all required files exist in the specified root directory.
        """
        try:
            VAL_STATUS = True
            if os.path.exists(self.config.data_ingestion_dir):
                list_of_files = os.listdir(self.config.data_ingestion_dir)
            else:
                logger.error(f"{self.config.data_ingestion_dir} does not exist.")
                VAL_STATUS = False
                with open(self.config.STATUS_FILE, "w") as status_file:
                    status_file.write(f"{VAL_STATUS}")
                return VAL_STATUS

            for file in self.config.REQUIRED_FILES:
                if file not in list_of_files:
                    logger.error(
                        f"Required file {file} not found in {self.config.data_ingestion_dir}"
                    )
                    VAL_STATUS = False
                    with open(self.config.STATUS_FILE, "w") as status_file:
                        status_file.write(f"{VAL_STATUS}")
                    return VAL_STATUS

            with open(self.config.STATUS_FILE, "w") as status_file:
                status_file.write(f"{VAL_STATUS}")

            return VAL_STATUS
        except Exception as e:
            logger.exception(f"Error occurred during data validation: {e}")
            VAL_STATUS = False
            return VAL_STATUS
