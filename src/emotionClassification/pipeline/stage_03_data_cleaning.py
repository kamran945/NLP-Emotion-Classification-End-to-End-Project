from src.emotionClassification.config.configuration import ConfigurationManager
from src.emotionClassification.components.data_cleaning import DataCleaning


class DataCleaningPipeline:

    def __init__(self) -> None:
        """Initialize the pipeline"""
        pass

    def main(self) -> dict:
        """Execute the pipeline"""

        config = ConfigurationManager()
        data_cleaning_config, data_cleaning_params = (
            config.get_data_cleaning_config_and_params()
        )

        data_cleaning = DataCleaning(
            config=data_cleaning_config, params=data_cleaning_params
        )
        cleaned_data = data_cleaning.save_and_return_cleaned_data()

        return cleaned_data
