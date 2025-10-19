from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import joblib

app = Flask(__name__, static_folder="static")
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Load your trained models, scaler, and feature selector (adjust paths as needed)
try:
    rf_model = joblib.load('models/random_forest_model.pkl')
    scaler = joblib.load('models/scaler.pkl')  # Load the scaler used during training
    feature_selector = joblib.load('models/feature_selector.pkl')  # Load the feature selector
    print("Model, scaler, and feature selector loaded successfully!")
except Exception as e:
    rf_model = None
    scaler = None
    feature_selector = None
    print(f"Warning: Could not load model/scaler/feature_selector. Error: {e}")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    # For now, redirect to home or create a simple about page
    return render_template("index.html")

@app.route("/contact")
def contact():
    # For now, redirect to home or create a simple contact page
    return render_template("index.html")

@app.route("/detection", methods=["GET", "POST"])
def detection():
    if request.method == "POST":
        # Handle file upload and prediction
        if 'csv_file' not in request.files:
            return render_template("detection.html", error="No file selected")
        
        file = request.files['csv_file']
        if file.filename == '':
            return render_template("detection.html", error="No file selected")
        
        if file and file.filename.lower().endswith('.csv'):
            try:
                # Read CSV file
                df = pd.read_csv(file)
                
                # Basic preprocessing - ensure column order matches training data
                # Remove ID and Label columns if they exist
                features = df.drop(columns=['ID', 'Label'], errors='ignore')
                
                # Ensure columns are in the exact same order as training data
                expected_columns = [
                    'I/O Data Operations', 'I/O Data Bytes', 'Number of subprocesses', 'Time on processor',
                    'Disk Reading/sec', 'Disc Writing/sec', 'Bytes Sent', 'Received Bytes (HTTP)',
                    'Network packets sent', 'Network packets received', 'Pages Read/sec', 'Pages Input/sec',
                    'Page Errors/sec', 'Confirmed byte radius'
                ]
                
                # Reorder columns to match training data
                features = features[expected_columns]
                
                # Make predictions using Random Forest model (primary model)
                if rf_model is not None and scaler is not None and feature_selector is not None:
                    # Apply the same scaling as used during training
                    features_scaled = pd.DataFrame(scaler.transform(features), columns=features.columns)
                    
                    # Apply feature selection - select the same top features as during training
                    features_selected = feature_selector.transform(features_scaled)
                    
                    # Make predictions using selected features
                    predictions = rf_model.predict(features_selected)
                    
                    # Calculate results
                    total_samples = len(predictions)
                    cryptojacking_detected = sum(predictions)
                    normal_samples = total_samples - cryptojacking_detected
                    
                    result = {
                        'total_samples': total_samples,
                        'cryptojacking_detected': cryptojacking_detected,
                        'normal_samples': normal_samples
                    }
                    
                    return render_template("detection.html", result=result)
                elif rf_model is None:
                    return render_template("detection.html", error="Detection model not available")
                elif scaler is None:
                    return render_template("detection.html", error="Scaler not available - please run the training notebook to save the scaler")
                else:
                    return render_template("detection.html", error="Feature selector not available - please run the training notebook to save the feature selector")
                    
            except Exception as e:
                return render_template("detection.html", error=f"Error processing file: {str(e)}")
        else:
            return render_template("detection.html", error="Please upload a valid CSV file")
    
    return render_template("detection.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    # Redirect to detection page
    return redirect(url_for('detection'))

@app.route("/form-detection", methods=["GET", "POST"])
def form_detection():
    if request.method == "POST":
        try:
            # Get form data and create DataFrame with exact column order from training data
            # This order must match the training data: Train.csv column order (excluding ID, Label)
            data_row = [
                float(request.form.get('io_data_operations', 0)),        # I/O Data Operations
                float(request.form.get('io_data_bytes', 0)),             # I/O Data Bytes  
                float(request.form.get('number_of_subprocesses', 0)),    # Number of subprocesses
                float(request.form.get('time_on_processor', 0)),         # Time on processor
                float(request.form.get('disk_reading_sec', 0)),          # Disk Reading/sec
                float(request.form.get('disc_writing_sec', 0)),          # Disc Writing/sec
                float(request.form.get('bytes_sent', 0)),                # Bytes Sent
                float(request.form.get('received_bytes_http', 0)),       # Received Bytes (HTTP)
                float(request.form.get('network_packets_sent', 0)),      # Network packets sent
                float(request.form.get('network_packets_received', 0)),  # Network packets received
                float(request.form.get('pages_read_sec', 0)),            # Pages Read/sec
                float(request.form.get('pages_input_sec', 0)),           # Pages Input/sec
                float(request.form.get('page_errors_sec', 0)),           # Page Errors/sec
                float(request.form.get('confirmed_byte_radius', 0))      # Confirmed byte radius
            ]
            
            # Create DataFrame with exact column names and order from training data
            column_names = [
                'I/O Data Operations', 'I/O Data Bytes', 'Number of subprocesses', 'Time on processor',
                'Disk Reading/sec', 'Disc Writing/sec', 'Bytes Sent', 'Received Bytes (HTTP)',
                'Network packets sent', 'Network packets received', 'Pages Read/sec', 'Pages Input/sec',
                'Page Errors/sec', 'Confirmed byte radius'
            ]
            
            df = pd.DataFrame([data_row], columns=column_names)
            
            # Make prediction using Random Forest model
            if rf_model is not None and scaler is not None and feature_selector is not None:
                # Apply the same scaling as used during training
                df_scaled = pd.DataFrame(scaler.transform(df), columns=df.columns)
                
                # Apply feature selection - select the same top features as during training
                df_selected = feature_selector.transform(df_scaled)
                
                # Make prediction using selected features
                prediction = rf_model.predict(df_selected)[0]
                probability = rf_model.predict_proba(df_selected)[0]
                
                # Get confidence score (probability of predicted class)
                confidence = max(probability) * 100
                
                result = {
                    'prediction': 'Cryptojacking Detected' if prediction == 1 else 'Normal Activity',
                    'confidence': round(confidence, 2),
                    'is_threat': prediction == 1
                }
                
                return render_template("form_detection.html", result=result)
            elif rf_model is None:
                return render_template("form_detection.html", error="Detection model not available")
            elif scaler is None:
                return render_template("form_detection.html", error="Scaler not available - please run the training notebook to save the scaler")
            else:
                return render_template("form_detection.html", error="Feature selector not available - please run the training notebook to save the feature selector")
                
        except Exception as e:
            return render_template("form_detection.html", error=f"Error processing data: {str(e)}")
    
    return render_template("form_detection.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)