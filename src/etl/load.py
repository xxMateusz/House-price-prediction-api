from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed" / "house_prices_clean.csv"

def load_data(df: pd.DataFrame) -> None:
    """
    Save processed data to disk.
    """
    PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)
