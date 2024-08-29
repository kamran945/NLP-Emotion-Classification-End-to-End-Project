from pathlib import Path
import os

from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
import yaml

from src.emotionClassification.logging import logger


@ensure_annotations
def read_yaml_file(filename: Path) -> ConfigBox:
    """
    Read a YAML file and return its contents as a ConfigBox.
    Args:
        filename (Path): Path to the YAML file.
    Raises:
        BoxValueError: If the YAML file is empty or malformed.
        Exception: If an error occurs while loading the YAML file.
    Returns:
        ConfigBox: Contents of the YAML file.
    """
    try:
        with open(filename, "r") as file:
            config_data = yaml.safe_load(file)
            logger.info(f"YAML file {filename} loaded successfully!")
            return ConfigBox(config_data)
    except BoxValueError as e:
        raise ValueError("YAML file is empty or malformed. ", e)
    except Exception as e:
        raise Exception(f"An error occurred while loading the YAML file: {str(e)}")


@ensure_annotations
def create_directories(filepath_list: list):
    """
    Create directories based on the provided file paths.
    Args:
        filepath_list (list): List of file paths.
    Raises:
        Exception: If an error occurs while creating directories.
    """
    for filepath in filepath_list:
        try:
            if not os.path.exists(filepath):
                os.makedirs(filepath, exist_ok=True)
                logger.info(f"Directory {filepath} created successfully!")
            else:
                logger.info(f"Directory {filepath} already exists!")
        except Exception as e:
            raise Exception(f"An error occurred while creating directory: {str(e)}")


@ensure_annotations
def get_directory_size(dir_path: str) -> float:
    """
    Get the total size of all files in a directory and its subdirectories in MB.
    Args:
        dir_path (str): Path to the directory.
    Returns:
        int: Total size of files in MB.
    """
    total_size = 0
    for dirpath, _, filenames in os.walk(dir_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size / (1024 * 1024)
