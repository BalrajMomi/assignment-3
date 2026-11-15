from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from src.config import RANDOM_STATE_SEED, MODEL_ESTIMATORS

def build_and_train_model(X_train_raw, y_train):
    # Set up categorical preprocessing pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'), X_train_raw.columns)
        ]
    )

    X_train = preprocessor.fit_transform(X_train_raw)

    # Train the Random Forest Classifier with configuration constraints
    rf_model = RandomForestClassifier(random_state=RANDOM_STATE_SEED, n_estimators=MODEL_ESTIMATORS)
    rf_model.fit(X_train, y_train)

    return rf_model, preprocessor
