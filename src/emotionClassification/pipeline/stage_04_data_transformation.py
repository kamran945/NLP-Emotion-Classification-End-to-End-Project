from src.emotionClassification.config.configuration import ConfigurationManager
from src.emotionClassification.components.data_transformation import DataTransformation


class DataTransformationPipeline:

    def __init__(self) -> None:
        """Initialize the pipeline"""
        pass

    def main(self) -> dict:
        """Execute the pipeline"""

        config = ConfigurationManager()
        data_transformation_config, data_transformation_params = (
            config.get_data_transformation_config_and_params()
        )

        data_transformation = DataTransformation(
            config=data_transformation_config, params=data_transformation_params
        )
        transformed_data = data_transformation.save_and_return_transformed_data()

        return transformed_data
