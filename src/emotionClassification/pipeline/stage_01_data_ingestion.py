from src.emotionClassification.config.configuration import ConfigurationManager
from src.emotionClassification.components.data_ingestion import DataIngestion


class DataIngestionTrainingPipeline:

    def __init__(self) -> None:
        """Initialize the pipeline"""
        pass

    def main(self) -> None:
        """Execute the pipeline"""

        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()

        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()
