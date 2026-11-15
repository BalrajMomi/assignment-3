import os
import urllib.request
import zipfile
import pandas as pd
from sklearn.model_selection import train_test_split
from src.config import DATASET_URL, ZIP_FILE_PATH, EXTRACT_DIRECTORY, DATA_FILE_NAME, DATASET_COLUMNS, TEST_SPLIT_SIZE, RANDOM_STATE_SEED

def download_and_load_data():
    if not os.path.exists(ZIP_FILE_PATH):
        print("Downloading dataset...")
        urllib.request.urlretrieve(DATASET_URL, ZIP_FILE_PATH)

    with zipfile.ZipFile(ZIP_FILE_PATH, 'r') as zip_ref:
        zip_ref.extractall(EXTRACT_DIRECTORY)

    data_path = os.path.join(EXTRACT_DIRECTORY, DATA_FILE_NAME)
    df = pd.read_csv(data_path, header=None, names=DATASET_COLUMNS)

    # Map classes to binary target
    y = df['class'].map({'e': 0, 'p': 1})
    X = df.drop(columns=['class'])

    return train_test_split(X, y, test_size=TEST_SPLIT_SIZE, random_state=RANDOM_STATE_SEED)
