"""
Demonstration script for cryptojacking detection using the form-based detection system.
This script shows how the Random Forest model with proper scaling works on sample data.
"""

import pandas as pd
import joblib
import numpy as np

def load_models():
    """Load the trained models and scaler"""
    try:
        rf_model = joblib.load('models/random_forest_model.pkl')
        scaler = joblib.load('models/scaler.pkl')
        print("✅ Models and scaler loaded successfully!")
        return rf_model, scaler
    except Exception as e:
        print(f"❌ Error loading models: {e}")
        return None, None

def create_sample_data():
    """Create sample data for testing (your original test data)"""
    sample_data = {
        'I/O Data Operations': 114.7988996,
        'I/O Data Bytes': 3790.450939,
        'Number of subprocesses': 28,
        'Time on processor': 0.427077829,
        'Disk Reading/sec': 6.162365173,
        'Disc Writing/sec': 21.22040265,
        'Bytes Sent': 58.49277265,
        'Received Bytes (HTTP)': 63.95938691,
        'Network packets sent': 0.621206167,
        'Network packets received': 0.52181318,
        'Pages Read/sec': 24.62461244,
        'Pages Input/sec': 0,
        'Page Errors/sec': 1001.53343,
        'Confirmed byte radius': 27.1908433
    }
    return sample_data

def create_normal_sample():
    """Create a sample that should be classified as normal"""
    normal_data = {
        'I/O Data Operations': 32.7094298,
        'I/O Data Bytes': 121124.1414,
        'Number of subprocesses': 30.40735917,
        'Time on processor': 0.496718733,
        'Disk Reading/sec': 3.999063766,
        'Disc Writing/sec': 0,
        'Bytes Sent': 335.565884,
        'Received Bytes (HTTP)': 737.3384903,
        'Network packets sent': 1.844012736,
        'Network packets received': 1.910663799,
        'Pages Read/sec': 0.311038293,
        'Pages Input/sec': 0,
        'Page Errors/sec': 726.318848,
        'Confirmed byte radius': 20.00868554
    }
    return normal_data

def predict_sample(rf_model, scaler, sample_data, sample_name):
    """Make prediction on a single sample"""
    
    print(f"\n{'='*50}")
    print(f"🔍 Testing: {sample_name}")
    print(f"{'='*50}")
    
    # Create DataFrame with exact column order from training
    df = pd.DataFrame([sample_data])
    
    # Apply scaling (same as used during training)
    df_scaled = pd.DataFrame(scaler.transform(df), columns=df.columns)
    
    # Make prediction
    prediction = rf_model.predict(df_scaled)[0]
    probabilities = rf_model.predict_proba(df_scaled)[0]
    
    # Get confidence score
    confidence = max(probabilities) * 100
    
    # Display results
    print(f"📊 Raw Input Data:")
    for feature, value in sample_data.items():
        print(f"   {feature}: {value}")
    
    print(f"\n🤖 Model Results:")
    print(f"   Prediction: {'🚨 CRYPTOJACKING DETECTED' if prediction == 1 else '✅ NORMAL ACTIVITY'}")
    print(f"   Confidence: {confidence:.2f}%")
    print(f"   Probability [Normal, Cryptojacking]: [{probabilities[0]:.4f}, {probabilities[1]:.4f}]")
    
    if prediction == 1:
        print(f"   ⚠️  THREAT LEVEL: HIGH - Immediate attention required!")
    else:
        print(f"   ✅ SYSTEM STATUS: Normal - No threats detected")
    
    return prediction, confidence

def main():
    """Main demonstration function"""
    
    print("🎯 Cryptojacking Detection Demonstration")
    print("=" * 60)
    
    # Load models
    rf_model, scaler = load_models()
    if rf_model is None or scaler is None:
        print("❌ Cannot proceed without models. Please ensure models are trained and saved.")
        return
    
    # Test Sample 1: Your original suspicious data
    suspicious_sample = create_sample_data()
    pred1, conf1 = predict_sample(rf_model, scaler, suspicious_sample, "Suspicious Activity Sample")
    
    # Test Sample 2: Normal activity
    normal_sample = create_normal_sample()
    pred2, conf2 = predict_sample(rf_model, scaler, normal_sample, "Normal Activity Sample")
    
    # Summary
    print(f"\n{'='*60}")
    print(f"📈 DETECTION SUMMARY")
    print(f"{'='*60}")
    print(f"Sample 1 (Suspicious): {'CRYPTOJACKING' if pred1 == 1 else 'NORMAL'} ({conf1:.1f}% confidence)")
    print(f"Sample 2 (Normal):     {'CRYPTOJACKING' if pred2 == 1 else 'NORMAL'} ({conf2:.1f}% confidence)")


if __name__ == "__main__":
    main()