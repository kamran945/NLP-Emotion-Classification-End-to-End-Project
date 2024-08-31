from box import ConfigBox


from datasets import load_from_disk
from transformers import AutoTokenizer
import datasets

from src.emotionClassification.logging import logger
from src.emotionClassification.entity import DataTransformationConfig


class DataTransformation:
    """
    Represents a data transformation process.
    """

    def __init__(self, config: DataTransformationConfig, params: ConfigBox) -> None:
        """
        Initialize the DataTransformation class with the given configuration.
        """
        self.config = config
        self.params = params
        self.tokenizer = AutoTokenizer.from_pretrained(params.model_checkpoint)
        self.class_labels = params.labels

    def tokenize(self, batch: datasets.Dataset) -> datasets.Dataset:
        """
        Tokenizes the text data in the input batch and adds the corresponding emotion labels.
        Args:
            batch: Input batch containing the text data and emotion labels.
        Returns:
            The input batch with tokenized text and emotion labels.
        """

        labels = [int(batch[label]) for label in self.class_labels]

        # Tokenize the text
        tokens = self.tokenizer(batch["Tweet"], padding=True, truncation=True)

        # Add the formatted labels to the tokenized output
        tokens.update({"labels": labels})

        return tokens

    def save_and_return_transformed_data(self) -> dict:
        """
        Save the transformed data to disk.
        """
        loaded_data = load_from_disk(self.config.data_cleaned_dir)
        transformed_data = loaded_data.map(self.tokenize, batched=False).remove_columns(
            ["ID", "Tweet"] + self.class_labels
        )

        transformed_data.save_to_disk(self.config.transformation_dir)

        return transformed_data
