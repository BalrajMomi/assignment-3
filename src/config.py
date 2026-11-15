# Configuration constants for the Mushroom Classification Application

DATASET_URL = 'https://archive.ics.uci.edu/static/public/73/mushroom.zip'
ZIP_FILE_PATH = 'mushroom.zip'
EXTRACT_DIRECTORY = 'mushroom_data'
DATA_FILE_NAME = 'agaricus-lepiota.data'

TEST_SPLIT_SIZE = 0.2
RANDOM_STATE_SEED = 42
MODEL_ESTIMATORS = 100

DATASET_COLUMNS = [
    'class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
    'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
    'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
    'stalk-surface-below-ring', 'stalk-color-above-ring',
    'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
    'ring-type', 'spore-print-color', 'population', 'habitat'
]
