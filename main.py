from src.emotionClassification.logging import logger
from src.emotionClassification.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from src.emotionClassification.pipeline.stage_02_data_validation import (
    DataValidationTrainingPipeline,
)

STAGE_NAME = "Data Ingestion"

try:
    logger.info(f">>>> Stage {STAGE_NAME} Started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> Stage {STAGE_NAME} Completed Successfully <<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation"

try:
    logger.info(f">>>> Stage {STAGE_NAME} Started <<<<")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> Stage {STAGE_NAME} Completed Successfully <<<<")
except Exception as e:
    logger.exception(e)
    raise e
