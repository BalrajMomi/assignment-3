from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def evaluate_predictions(y_true, y_pred):
    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred),
        "recall": recall_score(y_true, y_pred),
        "f1_score": f1_score(y_true, y_pred),
        "confusion_matrix": confusion_matrix(y_true, y_pred)
    }
    
    print("=== Model Evaluation Results ===")
    print(f"Accuracy:  {metrics['accuracy']:.4f}")
    print(f"Precision: {metrics['precision']:.4f}")
    print(f"Recall:    {metrics['recall']:.4f}")
    print(f"F1 Score:  {metrics['f1_score']:.4f}")
    print("Confusion Matrix:")
    print(metrics['confusion_matrix'])
    return metrics


def test_predictions(X_test_raw, y_test, preprocessor, rf_model):
    sample_indices = [1971, 6654, 5606]

    # 4. Generate predictions and print results
    for i, idx in enumerate(sample_indices, 1):
        print(f"=== Example {i} (Index {idx}) ===")
        print("Row Attributes:")
        print(X_test_raw.loc[idx].to_string())

        # Target label
        ground_truth_code = y_test.loc[idx]
        ground_truth_label = "poisonous (1)" if ground_truth_code == 1 else "edible (0)"

        # Model prediction
        sample_vector = preprocessor.transform(X_test_raw.loc[[idx]])
        prediction_code = rf_model.predict(sample_vector)[0]
        prediction_label = "poisonous (1)" if prediction_code == 1 else "edible (0)"

        print(f"\nGround Truth: {ground_truth_label}")
        print(f"Model Prediction: {prediction_label}")
        print("=" * 40 + "\n")