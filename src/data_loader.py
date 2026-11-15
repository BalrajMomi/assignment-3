import os
import urllib.request
import zipfile
import pandas as pd
from sklearn.model_selection import train_test_split

def download_and_load_data():
    url = 'https://archive.ics.uci.edu/static/public/73/mushroom.zip'
    zip_path = 'mushroom.zip'
    extract_dir = 'mushroom_data'

    if not os.path.exists(zip_path):
        print("Downloading dataset...")
        urllib.request.urlretrieve(url, zip_path)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)

    data_path = os.path.join(extract_dir, 'agaricus-lepiota.data')
    columns = [
        'class', 'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
        'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
        'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
        'stalk-surface-below-ring', 'stalk-color-above-ring',
        'stalk-color-below-ring', 'veil-type', 'veil-color', 'ring-number',
        'ring-type', 'spore-print-color', 'population', 'habitat'
    ]
    df = pd.read_csv(data_path, header=None, names=columns)
    
    y = df['class'].map({'e': 0, 'p': 1})
    X = df.drop(columns=['class'])
    
    # Return raw split data
    return train_test_split(X, y, test_size=0.2, random_state=42)
