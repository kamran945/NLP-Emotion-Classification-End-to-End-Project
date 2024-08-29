from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    extract_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    data_ingestion_dir: Path
    STATUS_FILE: str
    REQUIRED_FILES: list
