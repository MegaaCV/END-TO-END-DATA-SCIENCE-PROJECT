# END-TO-END-DATA-SCIENCE-PROJECT

COMPANY NAME : CODETECH IT SOLUTIONS

NAME : MEGAA C V

INTERN ID : CT06DN683

DOMAIN : DATA SCIENCE

DURATION : 6 WEEKS

MENTOR : NEELA SANTHOSH

# Description of this project

COMPANY NAME : CODETECH IT SOLUTIONS

# 🏠 House Price Prediction API

A modern web application built with FastAPI that provides real-time house price predictions using machine learning. Features an intuitive web interface for users to input property details and receive instant price estimates.

## 🚀 Features

- **Interactive Web Form**: User-friendly interface for inputting house features
- **Real-time Predictions**: Instant price predictions using a pre-trained ML model
- **RESTful API**: Clean API endpoints for programmatic access
- **Automatic Documentation**: Interactive API docs with Swagger UI
- **Input Validation**: Robust data validation and error handling
- **Responsive Design**: Mobile-friendly web interface
- **Docker Support**: Easy containerization and deployment

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Docker (optional, for containerized deployment)

## 🛠️ Installation

### Local Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd house-price-prediction-api
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure model files are present**
   - `housing_price_model.pkl` (trained ML model)
   - `feature_columns.pkl` (feature column names)

### Docker Setup

1. **Build the Docker image**
   ```bash
   docker build -t house-price-api .
   ```

2. **Run the container**
   ```bash
   docker run -p 8000:8000 house-price-api
   ```

## 🚀 Usage

### Starting the Application

**Option 1: Using uvicorn directly**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

**Option 2: Using the startup script**
```bash
bash start_server.sh
```

### Accessing the Application

- **Web Interface**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

## 🏡 Sample Input

Use these sample values to test the application:

| Feature | Value |
|---------|-------|
| Area (sq ft) | 7500 |
| Bedrooms | 4 |
| Bathrooms | 2 |
| Stories | 3 |
| Parking Spaces | 2 |
| Main Road Access | Yes |
| Guest Room | No |
| Basement | No |
| Hot Water Heating | No |
| Air Conditioning | Yes |
| Preferred Area | Yes |
| Furnishing Status | Furnished |

## 📊 API Endpoints

### Web Interface
- `GET /` - Interactive web form for price prediction

### API Endpoints
- `GET /health` - Health check endpoint
- `GET /model-info` - Information about the ML model and features
- `POST /predict` - Programmatic price prediction

### Example API Usage

```python
import requests

# Prediction request
data = {
    "area": 7500,
    "bedrooms": 4,
    "bathrooms": 2,
    "stories": 3,
    "parking": 2,
    "mainroad": "yes",
    "guestroom": "no",
    "basement": "no",
    "hotwaterheating": "no",
    "airconditioning": "yes",
    "prefarea": "yes",
    "furnishingstatus": "furnished"
}

response = requests.post("http://localhost:8000/predict", json=data)
print(response.json())
```

## 🏗️ Project Structure

```
house-price-prediction-api/
├── main.py                    # FastAPI application
├── requirements.txt           # Python dependencies
├── start_server.sh           # Server startup script
├── test_client.py            # API test client
├── Dockerfile                # Docker configuration
├── templates/                # HTML templates
│   └── index.html            # Web form template
├── housing_price_model.pkl   # Trained ML model
├── feature_columns.pkl       # Feature column names
└── README.md                 # Project documentation
```

## 🔧 Configuration

### Environment Variables

- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8000)
- `RELOAD`: Enable auto-reload in development (default: True)

### Model Requirements

The application expects two pickle files:
- `housing_price_model.pkl`: Trained scikit-learn model
- `feature_columns.pkl`: List of feature column names used during training

## 📈 Model Information

The prediction model uses the following features:

**Numerical Features:**
- Area (square feet)
- Number of bedrooms
- Number of bathrooms
- Number of stories
- Parking spaces

**Categorical Features:**
- Main road access (yes/no)
- Guest room (yes/no)
- Basement (yes/no)
- Hot water heating (yes/no)
- Air conditioning (yes/no)
- Preferred area (yes/no)
- Furnishing status (furnished/semi-furnished/unfurnished)


