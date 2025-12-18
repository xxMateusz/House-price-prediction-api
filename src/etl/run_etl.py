from extract import extract_data
from transform import transform_data
from load import load_data

def run_etl():
    df_raw = extract_data()
    df_clean = transform_data(df_raw)
    load_data(df_clean)

if __name__ == "__main__":
    run_etl()
