import os
from pathlib import Path
from box import ConfigBox

import re
import nltk
from nltk.corpus import stopwords
import emoji
import contractions
from autocorrect import Speller
import pandas as pd
import string
from datasets import load_from_disk

from src.emotionClassification.logging import logger
from src.emotionClassification.entity import DataCleaningConfig


class DataCleaning:
    """
    Represents a data cleaning process.
    """

    def __init__(self, config: DataCleaningConfig, params: ConfigBox) -> None:
        """
        Initialize the DataCleaning class with the given configuration.
        """
        self.config = config
        self.params = params

    def clean_data(self, batch: dict) -> dict:
        """
        Cleans the text data in the input batch.
        Args:
            batch: Input batch containing the text data.
        Returns:
            The input batch with preprocessed text.
        """
        text = batch["Tweet"]
        series = pd.Series(text)  # To Speed up operations on batch

        # Apply preprocessing steps using vectorized operations
        series = series.apply(lambda x: contractions.fix(x))  # Expand contractions
        series = series.str.lower()  # Lowercase
        series = series.str.replace(
            r"http\S+|www\S+|https\S+", "", regex=True
        )  # Remove URLs
        series = series.str.replace(r"@\w+", "", regex=True)  # Remove mentions
        series = series.str.replace(
            r"[^\w\s]", "", regex=True
        )  # Remove special characters
        series = series.str.replace(r"(.)\1+", r"\1\1", regex=True)  # Handle elongation
        series = series.str.replace(
            f"[{string.punctuation}]", "", regex=True
        )  # Remove punctuation

        #     # Remove stopwords
        #     def remove_stopwords(text):
        #         words = text.split()
        #         filtered_words = [word for word in words if word not in stop_words]
        #         return ' '.join(filtered_words)
        #     series = series.apply(remove_stopwords)

        series = series.apply(lambda x: emoji.demojize(x))  # Convert emojis to text
        text = series.tolist()
        batch["Tweet"] = text

        return batch

    def save_and_return_cleaned_data(self) -> dict:
        """
        Save the cleaned data to disk.
        """
        loaded_data = load_from_disk(self.config.data_ingestion_dir)
        cleaned_data = loaded_data.map(
            self.clean_data, batched=True, batch_size=self.params.batch_size
        )
        cleaned_data.save_to_disk(self.config.cleaned_dir)

        return cleaned_data
