from src.data_loader import download_and_load_data
from src.model import build_and_train_model
from src.evaluation import evaluate_predictions, test_predictions

def main():
    print("Initializing Modular Mushroom Classification Pipeline...")
    X_train_raw, X_test_raw, y_train, y_test = download_and_load_data()
    
    model, preprocessor = build_and_train_model(X_train_raw, y_train)
    
    X_test = preprocessor.transform(X_test_raw)
    y_pred = model.predict(X_test)
    
    evaluate_predictions(y_test, y_pred)

    test_predictions(X_test_raw, y_test, preprocessor, model)

if __name__ == '__main__':
    main()
