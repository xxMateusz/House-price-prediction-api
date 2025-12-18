from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import pandas as pd
import numpy as np
import joblib

# Inicjalizacja FastAPI
app = FastAPI(title="House Price Predictor API")

# Wczytanie modelu
MODEL_PATH = "data/processed/xgb_pipeline.joblib"
model = joblib.load(MODEL_PATH)
print(f"Model wczytany z: {MODEL_PATH}")

# Schema Pydantic
class House(BaseModel):
    MSSubClass: int
    MSZoning: str
    LotFrontage: float
    LotArea: int
    Street: str
    Alley: Optional[str] = None
    LotShape: str
    LandContour: str
    Utilities: str
    LotConfig: str
    LandSlope: str
    Neighborhood: str
    Condition1: str
    Condition2: str
    BldgType: str
    HouseStyle: str
    OverallQual: int
    OverallCond: int
    YearBuilt: int
    YearRemodAdd: int
    RoofStyle: str
    RoofMatl: str
    Exterior1st: str
    Exterior2nd: str
    MasVnrType: str
    MasVnrArea: float
    ExterQual: str
    ExterCond: str
    Foundation: str
    BsmtQual: str
    BsmtCond: str
    BsmtExposure: str
    BsmtFinType1: str
    BsmtFinSF1: float
    BsmtFinType2: str
    BsmtFinSF2: float
    BsmtUnfSF: float
    TotalBsmtSF: float
    Heating: str
    HeatingQC: str
    CentralAir: str
    Electrical: str
    FirstFlrSF: float       # będzie zamienione na 1stFlrSF
    SecondFlrSF: float      # będzie zamienione na 2ndFlrSF
    LowQualFinSF: float
    GrLivArea: float
    BsmtFullBath: float
    BsmtHalfBath: float
    FullBath: float
    HalfBath: float
    BedroomAbvGr: int
    KitchenAbvGr: int
    KitchenQual: str
    TotRmsAbvGrd: int
    Functional: str
    Fireplaces: int
    FireplaceQu: Optional[str] = None
    GarageType: str
    GarageYrBlt: float
    GarageFinish: str
    GarageCars: float
    GarageArea: float
    GarageQual: str
    GarageCond: str
    PavedDrive: str
    WoodDeckSF: float
    OpenPorchSF: float
    EnclosedPorch: float
    ThreeSsnPorch: float    # będzie zamienione na 3SsnPorch
    ScreenPorch: float
    PoolArea: float
    PoolQC: Optional[str] = None
    Fence: Optional[str] = None
    MiscFeature: Optional[str] = None
    MiscVal: float
    MoSold: int
    YrSold: int
    SaleType: str
    SaleCondition: str

# Endpoint predykcji
@app.post("/predict")
def predict(house: House):
    # Konwersja obiektu Pydantic na DataFrame
    data = pd.DataFrame([house.dict()])

    # Zamiana nazw kolumn na te wymagane przez model
    data.rename(columns={
        "FirstFlrSF": "1stFlrSF",
        "SecondFlrSF": "2ndFlrSF",
        "ThreeSsnPorch": "3SsnPorch"
    }, inplace=True)

    # Sprawdzenie brakujących kolumn
    missing_cols = set(model.feature_names_in_) - set(data.columns)
    if missing_cols:
        return {"error": f"Brakuje kolumn: {missing_cols}"}

    # Predykcja log(ceny)
    try:
        pred_log = model.predict(data)[0]
        pred = float(pred_log)   # <-- KLUCZOWA LINIA

        return {
          "prediction": pred
      }

    except Exception as e:
        return {"error": str(e)}
@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_loaded": True
    }
