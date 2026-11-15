from src.data_loader import download_and_load_data
from src.model import build_and_train_model
from src.evaluation import evaluate_predictions

def main():
    # 1. Download and load split dataset
    X_train_raw, X_test_raw, y_train, y_test = download_and_load_data()
    
    # 2. Build and train Random Forest model with preprocessing pipeline
    model, preprocessor = build_and_train_model(X_train_raw, y_train)
    
    # 3. Preprocess test attributes and predict
    X_test = preprocessor.transform(X_test_raw)
    y_pred = model.predict(X_test)
    
    # 4. Evaluate performance parameters
    evaluate_predictions(y_test, y_pred)

if __name__ == '__main__':
    main()
