from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier

def build_and_train_model(X_train_raw, y_train):
    # Set up preprocessing pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'), X_train_raw.columns)
        ]
    )
    
    # Encode training attributes
    X_train = preprocessor.fit_transform(X_train_raw)
    
    # Train Random Forest Classifier
    rf_model = RandomForestClassifier(random_state=42, n_estimators=100)
    rf_model.fit(X_train, y_train)
    
    return rf_model, preprocessor
