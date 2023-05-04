# Facial Expression Recognition

This project converts feature and label data into an ARFF format file for facial expression recognition.

## Installation

1. Clone the repository:
   `git clone https://github.com/example/facial-expression-recognition.git`
2. Install the required packages:
   `pip install -r requirements.txt`

## Usage

`python facial_expression_recognition.py [FEATURE_FILE] [LABEL_FILE] [OUTPUT_FILE] [--config CONFIG_FILE] [--scale {minmax,standard}]`

### Arguments

- **FEATURE_FILE**: Path to the file containing feature data.
- **LABEL_FILE**: Path to the file containing label data.
- **OUTPUT_FILE**: Path to the output ARFF file.
- **--config**: Path to the configuration file (default: config.yaml).
- **--scale**: Apply scaling to numeric features. Choices: minmax, standard.

### Configuration

The **config.yaml** file contains the following configuration settings:

- **relation_name**: Name of the relation in the ARFF file.
- **class_name**: Name of the class attribute in the ARFF file.
- **class_values**: Possible values for the class attribute.
- **feature_key_format**: Format string for the feature data keys in the input files.
- **label_key_format**: Format string for the label data keys in the input files.
- **feature_data_types**: Data types of the feature attributes in the ARFF file.
