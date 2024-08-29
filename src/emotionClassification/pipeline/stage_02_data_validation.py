from src.emotionClassification.config.configuration import ConfigurationManager
from src.emotionClassification.components.data_validation import DataValidation


class DataValidationTrainingPipeline:

    def __init__(self) -> None:
        """Initialize the pipeline"""
        pass

    def main(self) -> bool:
        """Execute the pipeline"""

        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()

        data_validation = DataValidation(config=data_validation_config)
        val_status = data_validation.validate_all_required_files_exist()
        print(f"Validation Status: {val_status}")

        return val_status
