import os
import pandas as pd

RAW_DIR = "/workspaces/data-analysis-3/airbnb-price-model/data/raw"

def load_listings(filename: str, snapshot: str) -> pd.DataFrame:
    path = os.path.join(RAW_DIR, filename)
    df = pd.read_csv(path, low_memory=False)  # works for .csv and .csv.gz
    df["snapshot"] = snapshot
    return df

ams_q1 = load_listings("amsterdam-2025q1-listings.csv.gz", "amsterdam_q1_2025")
ams_q3 = load_listings("amsterdam-2025q3-listings.csv.gz", "amsterdam_q3_2025") 
brussels_q3 = load_listings("brussels-2025q3-listings.csv.gz", "brussels_q3_2025")