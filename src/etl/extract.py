from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DATA_PATH = BASE_DIR / "data" / "train.csv"
def extract_data() -> pd.DataFrame:
    """
    Load raw house prices data.
    """
    df = pd.read_csv(RAW_DATA_PATH)
    return df
