from src.emotionClassification.logging import logger
from src.emotionClassification.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from src.emotionClassification.pipeline.stage_02_data_validation import (
    DataValidationTrainingPipeline,
)
from src.emotionClassification.pipeline.stage_03_data_cleaning import (
    DataCleaningPipeline,
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


STAGE_NAME = "Data Cleaning/Preprocessing"

try:
    logger.info(f">>>> Stage {STAGE_NAME} Started <<<<")
    data_cleaning = DataCleaningPipeline()
    cleanined_data = data_cleaning.main()
    logger.info(f">>>> Stage {STAGE_NAME} Completed Successfully <<<<")
except Exception as e:
    logger.error(f">>>> Stage {STAGE_NAME} Failed <<<<")
    logger.exception(e)
    raise e
