import json
import argparse
import os
import yaml
from typing import Dict


class DataReader:
    """Reads data from feature and label files."""

    @staticmethod
    def read_data(file_path: str):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data


class DataValidator:
    """Validates feature and label data."""

    @staticmethod
    def validate_data(feature_data, label_data):
        if len(feature_data) != len(label_data):
            raise ValueError("Feature and label data lengths do not match.")


class ARFFWriter:
    """Writes feature and label data to an ARFF file."""

    def __init__(self, feature_data, label_data, output_file, config):
        self.feature_data = feature_data
        self.label_data = label_data
        self.output_file = output_file
        self.config = config

    def write_arff_file(self):
        with open(self.output_file, "w") as file:
            self.write_relation(file)
            self.write_attributes(file)
            self.write_data(file)

    def write_relation(self, file):
        file.write(f"@RELATION {self.config['relation_name']}\n\n")

    def write_attributes(self, file):
        for i, feature_dtype in enumerate(self.config['feature_data_types']):
            file.write(f"@ATTRIBUTE feature{i} {feature_dtype}\n")
        file.write(
            f"@ATTRIBUTE {self.config['class_name']} {{{','.join(self.config['class_values'])}}}\n\n")

    def write_data(self, file):
        file.write("@DATA\n")
        for i in range(len(self.feature_data)):
            data_key = self.config['feature_key_format'].format(i)
            file.write(",".join(map(str, self.feature_data[data_key]["data"])))
            file.write(
                "," + str(self.label_data[self.config['label_key_format'].format(i)]))
            file.write("\n")


class FeatureScaler:
    """Scales numeric features using Min-Max scaling or standardization."""

    def __init__(self, method, config):
        self.method = method
        self.config = config

    def scale_features(self, feature_data):
        for i in range(len(feature_data)):
            data_key = self.config['feature_key_format'].format(i)
            values = feature_data[data_key]['data']
            if self.method == 'minmax':
                min_value, max_value = min(values), max(values)
                values = [(x - min_value) / (max_value - min_value)
                          for x in values]
            elif self.method == 'standard':
                mean_value = sum(values) / len(values)
                std_dev = (
                    sum((x - mean_value) ** 2 for x in values) / len(values)) ** 0.5
                values = [(x - mean_value) / std_dev for x in values]
            else:
                return feature_data
            feature_data[data_key]['data'] = values
        return feature_data


def read_config_file(file_path: str) -> Dict:
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config


def get_args() -> argparse.Namespace:
    """
    Parses command line arguments.

    Returns:
        argparse.Namespace: The parsed command line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Convert feature and label data to ARFF format.")
    parser.add_argument(
        "feature_file",
        nargs="?",
        help="Path to the file containing feature data."
    )
    parser.add_argument(
        "label_file",
        nargs="?",
        help="Path to the file containing label data."
    )
    parser.add_argument(
        "output_file",
        nargs="?",
        help="Path to the output ARFF file."
    )
    parser.add_argument(
        "--config",
        default="config.yaml",
        help="Path to the configuration file (default: 'config.yaml')."
    )
    parser.add_argument(
        "--scale",
        choices=["minmax", "standard"],
        help="Apply scaling to numeric features. Choices: 'minmax', 'standard'."
    )
    return parser.parse_args()
