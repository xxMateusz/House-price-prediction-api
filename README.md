# House Price Prediction API 🏡💰

Predict house prices using a trained XGBoost model with a FastAPI backend. This project is built as a professional-ready ML API with Docker support.

---

## 🚀 Features

- **Predict house prices** based on Ames Housing dataset features.
- **Batch predictions** support multiple items at once.
- **Dockerized** for easy deployment.
- **Health check endpoint** to verify model is loaded.
- **Data validation** for required input fields.

---

## 🧰 Tech Stack

- **Backend:** FastAPI
- **Model:** XGBoost (pretrained pipeline)
- **Data processing:** Pandas, Scikit-learn
- **Deployment:** Docker
- **Language:** Python 3.11

---

## 📂 Project Structure

ds+de/
│
├── api/ # FastAPI application
│ └── main.py
├── data/
│ └── processed/
│ └── xgb_pipeline.joblib
├── Dockerfile
├── requirements.txt
└── README.md


---

## ⚡ Quick Start

### 1️⃣ Build Docker image
```bash
docker build -t house-api .
2️⃣ Run Docker container
bash
Skopiuj kod
docker run -p 8000:8000 house-api
API will be accessible at: http://127.0.0.1:8000

Swagger UI (Try it out): http://127.0.0.1:8000/docs

📝 Endpoints
1. GET /health
Check if the API is up and model is loaded.

Response:

json
Skopiuj kod
{
  "status": "ok",
  "model_loaded": true
}
2. POST /predict
Predict price for a single house.

Request Example:

json
Skopiuj kod
{
  "LotArea": 8450,
  "OverallQual": 7,
  "YearBuilt": 2003,
  "GrLivArea": 1710,
  "FullBath": 2,
  "BedroomAbvGr": 3,
  "KitchenAbvGr": 1,
  "TotRmsAbvGrd": 8,
  "Fireplaces": 0,
  "GarageCars": 2,
  "GarageArea": 548,
  "1stFlrSF": 856,
  "2ndFlrSF": 854,
  "3SsnPorch": 0,
  "PoolQC": null,
  "Fence": null,
  "MiscFeature": null,
  "MiscVal": 0,
  "MoSold": 5,
  "YrSold": 2008,
  "SaleType": "WD",
  "SaleCondition": "Normal"
}
Response Example:

json
Skopiuj kod
{
  "predicted_price": 208500.0
}
3. POST /predict_batch
Predict multiple houses at once.

Request Example:

json
Skopiuj kod
{
  "items": [
    {
      "LotArea": 8450,
      "OverallQual": 7,
      "YearBuilt": 2003,
      "GrLivArea": 1710
    },
    {
      "LotArea": 9600,
      "OverallQual": 6,
      "YearBuilt": 1976,
      "GrLivArea": 1262
    }
  ]
}
Response Example:

json
Skopiuj kod
{
  "predictions": [208500.0, 181500.0]
}
🛠 Requirements
Python 3.11

FastAPI

Uvicorn

Pandas

Scikit-learn

XGBoost

Joblib

Install dependencies:

bash
Skopiuj kod
pip install -r requirements.txt
📈 Model Info
Type: XGBoost Regression Pipeline

Dataset: Ames Housing

Features: Numeric + Categorical features (processed in pipeline)

Trained in: Jupyter Notebook (Python 3.11)

Serialization: joblib

⚡ Notes
Ensure data/processed/xgb_pipeline.joblib exists before running the API.

All categorical columns must be strings; missing values are handled internally.

Designed to run locally via Docker or can be deployed on cloud platforms.

📖 License
MIT License
