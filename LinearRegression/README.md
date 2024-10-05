Here's a comprehensive README for your Flask-based **House Price Predictor** application. This README is structured to give users and developers a clear understanding of the project, setup instructions, and usage.

---

# House Price Predictor

A web application that predicts house prices based on several input parameters such as area (sq ft), bedrooms, bathrooms, stories, and parking spaces. The backend uses a **Linear Regression** model trained on housing data, while the front-end collects user inputs and displays the predicted price.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features
- Predict house prices based on:
  - Area (in square feet)
  - Number of bedrooms
  - Number of bathrooms
  - Number of stories
  - Available parking spaces
- Linear Regression model trained on real estate data
- Front-end form for user input
- RESTful API for prediction
- Cross-Origin Resource Sharing (CORS) support for front-end and back-end communication

## Project Structure

```
house_price_predictor/
├── app.py               # Flask backend (main server script)
├── Housing.csv          # Dataset for training the model
├── requirements.txt     # Python dependencies
├── static/
│   ├── style.css        # CSS for front-end styling
│   └── script.js        # JavaScript for form submission and API call
└── templates/
    └── index.html       # HTML front-end form for input and result display
```

## Requirements

- Python 3.x
- Flask
- scikit-learn
- pandas
- Flask-CORS

### Dependencies (Python Packages)
- Flask==2.x
- Flask-CORS==3.x
- scikit-learn==1.x
- pandas==2.x

You can find all dependencies in the `requirements.txt` file.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/house-price-predictor.git
cd house-price-predictor
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add the Dataset
Ensure the `Housing.csv` dataset is located in the project root directory. If you don’t have the dataset, you can either:
- Download a housing dataset from [Kaggle](https://www.kaggle.com/) or
- Use your own dataset and ensure it has the correct columns (like `area`, `bedrooms`, `price`, etc.).

### 5. Run the Flask Application
```bash
python app.py
```

By default, the app will run at `http://127.0.0.1:5000/`.

### 6. Open the Application
Open your browser and navigate to `http://127.0.0.1:5000/` to access the front-end form.

## Usage

### 1. Web Interface
- Go to the home page of the application.
- Enter values for:
  - **Area** (in square feet)
  - **Bedrooms**
  - **Bathrooms**
  - **Stories**
  - **Parking Spaces**
- Click the **Predict Price** button.
- The predicted house price will be displayed on the screen.

### 2. API Endpoint
You can also interact with the app via its API. Send a POST request with a JSON payload to `/predict`.

Example POST request:

```bash
curl -X POST http://127.0.0.1:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"area": 1500, "bedrooms": 3, "bathrooms": 2, "stories": 2, "parking": 1}'
```

Response:
```json
{
  "prediction": 325000.0
}
```

### Example Front-end Form
The front-end form allows users to input values directly in the browser to get the predicted price.

## Dataset

The model is trained on the **Housing.csv** dataset, which includes various features such as:
- `price` (target)
- `area` (in square feet)
- `bedrooms`, `bathrooms`, `stories`, `parking`
- Categorical features such as `mainroad`, `guestroom`, `basement`, etc.

### Dataset Columns:

| Feature            | Description                 |
|--------------------|-----------------------------|
| `price`            | Target (house price)         |
| `area`             | Area in square feet          |
| `bedrooms`         | Number of bedrooms           |
| `bathrooms`        | Number of bathrooms          |
| `stories`          | Number of stories            |
| `parking`          | Parking spaces available     |
| `mainroad`         | Access to main road (yes/no) |
| `guestroom`        | Guest room availability      |

## API Endpoints

### POST `/predict`

- **Description**: Predict house price based on the input parameters.
- **Request Body**: JSON with the following fields:
  - `area` (float): Area in square feet.
  - `bedrooms` (int): Number of bedrooms.
  - `bathrooms` (int): Number of bathrooms.
  - `stories` (int): Number of stories.
  - `parking` (int): Parking spaces.
  
- **Response**: JSON object with the predicted price.

Example:
```json
{
  "prediction": 325000.0
}
```

### Error Handling
If the request is invalid (e.g., missing fields), the API returns a 400 error with an error message:
```json
{
  "error": "Missing columns: bathrooms, parking"
}
```

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
