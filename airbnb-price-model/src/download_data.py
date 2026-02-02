from __future__ import annotations
import os
from pathlib import Path
import requests

RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

# Fill these with the direct "listings.csv.gz" links from InsideAirbnb
DATASETS = {
    # Amsterdam
    "amsterdam-2025q1-listings.csv.gz": "https://data.insideairbnb.com/the-netherlands/north-holland/amsterdam/2025-03-02/data/listings.csv.gz",
    "amsterdam-2025q3-listings.csv.gz": "https://data.insideairbnb.com/the-netherlands/north-holland/amsterdam/2025-09-11/data/listings.csv.gz",

    # Brussels
    "brussels-2025q3-listings.csv.gz": "https://data.insideairbnb.com/belgium/bru/brussels/2025-09-23/data/listings.csv.gz",
}

def download(url: str, dest: Path) -> None:
    print(f"Downloading -> {dest.name}")
    with requests.get(url, stream=True, timeout=60) as r:
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

def main():
    missing = [k for k, v in DATASETS.items() if "PASTE_URL_HERE" in v]
    if missing:
        print("ERROR: Please paste the InsideAirbnb URLs for:")
        for m in missing:
            print(" -", m)
        raise SystemExit(1)

    for filename, url in DATASETS.items():
        dest = RAW_DIR / filename
        if dest.exists():
            print(f"Already exists, skipping: {filename}")
            continue
        download(url, dest)

    print("\nDone. You can now run the notebook.")
    print("Tip: pandas can read .csv.gz directly with pd.read_csv('file.csv.gz').")

if __name__ == "__main__":
    main()



