#!/usr/bin/env python3

import pandas as pd
import joblib

def test_with_known_samples():
    """Test with known cryptojacking samples from training data"""
    
    # Load models and scaler
    try:
        rf_model = joblib.load('models/random_forest_model.pkl')
        scaler = joblib.load('models/scaler.pkl')
        print("✓ Models and scaler loaded successfully!")
    except Exception as e:
        print(f"✗ Error loading models: {e}")
        return
    
    # Load training data to get some known cryptojacking samples
    train_df = pd.read_csv('dataset/Train.csv')
    
    # Get some cryptojacking samples (Label = 1)
    crypto_samples = train_df[train_df['Label'] == 1].head(10)
    normal_samples = train_df[train_df['Label'] == 0].head(10)
    
    # Combine for testing
    test_samples = pd.concat([crypto_samples, normal_samples])
    
    print(f"Testing with {len(crypto_samples)} cryptojacking and {len(normal_samples)} normal samples")
    
    # Preprocess
    features = test_samples.drop(columns=['ID', 'Label'])
    actual_labels = test_samples['Label'].values
    
    # Scale features
    features_scaled = pd.DataFrame(scaler.transform(features), columns=features.columns)
    
    # Predict
    predictions = rf_model.predict(features_scaled)
    probabilities = rf_model.predict_proba(features_scaled)
    
    print("\nResults:")
    print(f"Actual cryptojacking samples: {sum(actual_labels)}")
    print(f"Predicted cryptojacking samples: {sum(predictions)}")
    print(f"Accuracy: {sum(predictions == actual_labels) / len(actual_labels) * 100:.1f}%")
    
    # Show individual results
    print("\nDetailed Results:")
    for i in range(len(predictions)):
        actual = "CRYPTO" if actual_labels[i] == 1 else "NORMAL"
        predicted = "CRYPTO" if predictions[i] == 1 else "NORMAL"
        confidence = max(probabilities[i]) * 100
        match = "✓" if actual_labels[i] == predictions[i] else "✗"
        print(f"{match} Actual: {actual:6} | Predicted: {predicted:6} | Confidence: {confidence:5.1f}%")

if __name__ == "__main__":
    test_with_known_samples()