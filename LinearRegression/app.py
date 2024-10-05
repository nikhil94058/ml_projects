# app.py (Flask Backend)
from flask import Flask, request, jsonify
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Load your dataset
db = pd.read_csv('Housing.csv')  # Replace with the correct path to your dataset

# Preprocess the data (e.g., one-hot encoding)
db_encoded = pd.get_dummies(db, columns=[
    'mainroad', 'guestroom', 'basement', 
    'hotwaterheating', 'airconditioning', 
    'prefarea', 'furnishingstatus'
], drop_first=True)

# Prepare features and target
X = db_encoded.drop(columns=['price'])  # Features
y = db_encoded['price']  # Target

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from the request (as JSON)
        data = request.get_json()
        print("Received data:", data)  # Log the received data for debugging

        # Check if input data is provided
        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        # Convert the input data to a DataFrame
        input_data = pd.DataFrame([data])

        # Ensure all required columns are present in the input data
        missing_cols = set(X.columns) - set(input_data.columns)
        if missing_cols:
            # Add missing columns with default value 0
            for col in missing_cols:
                input_data[col] = 0

        # Reorder the input data columns to match the training data
        input_data = input_data[X.columns]

        # Perform prediction
        prediction = model.predict(input_data)

        # Return the prediction as JSON
        return jsonify({'prediction': prediction[0]})

    except ValueError as e:
        # Handle errors related to data processing or prediction
        return jsonify({'error': f'ValueError: {str(e)}'}), 400
    
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
