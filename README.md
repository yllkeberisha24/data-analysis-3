# data-analysis-3
## Project: Airbnb Price Prediction (InsideAirbnb)

This project builds pricing models for Airbnb listings using InsideAirbnb data.
Models are trained on Amsterdam Q1 2025 and evaluated for:
- Temporal validity (Amsterdam Q3 2025)
- Geographic validity (Brussels Q3 2025)



### Data

Data is sourced from InsideAirbnb (https://insideairbnb.com/get-the-data/).

---

### Datasets used

- Amsterdam Q1 2025 — training data (10,075 listings)

- Amsterdam Q3 2025 — temporal validity dataset (10,480 listings)

- Brussels Q3 2025 — geographic validity dataset (6,131 listings)

Raw data files are not committed to the repository due to size constraints.
They can be downloaded automatically using the provided script.

---

### Feature Engineering

The following features are constructed and used across all models:

- Cleaned nightly price (price_clean)

- Listing size and capacity (e.g. accommodates, bedrooms)

- Room type (one-hot encoded)

- Availability and review activity

- Amenity information:

    - parsed amenity lists

    - total number of amenities

    - binary indicators for the top 50 amenities (based on training data only)

The target variable is log-transformed price, which reduces skewness and improves model stability.

--- 

### Models

Five predictive models are estimated and compared:

1. Ordinary Least Squares (OLS)

2. LASSO (with cross-validation)

3. Random Forest

4. Gradient Boosting

5. Extra Trees

Models are evaluated using:

- RMSE in log-price space

- R²

- Training time

A horserace table compares predictive accuracy and computational cost.

--- 

## Key Results
### Model Performance (Amsterdam Q1)

Tree-based models substantially outperform linear models, indicating nonlinearities and interaction effects in Airbnb pricing. Gradient Boosting achieves the best overall predictive performance.

--- 

### Feature Importance

Across Random Forest and Gradient Boosting models, the most important predictors include:

- number of bedrooms

- room type (entire home vs private room)

- listing capacity

- availability and review activity

- amenity richness

This suggests that both physical characteristics and market engagement play a key role in pricing.

--- 

### Validity Analysis

- **Temporal validity**: Models generalize well from Amsterdam Q1 to Amsterdam Q3, indicating stable pricing relationships over time within the same city.

- **Geographic validity**: Performance deteriorates sharply when applied to Brussels, with negative R² values across all models. This highlights the city-specific nature of Airbnb pricing and limited geographic transferability without retraining.
--- 

### Reproducibility
Setup

```bash 
pip install -r requirements.txt
```

Download data
```bash
python airbnb-price-model/src/download_data.py
```
Data Loading

Once the data is downloaded, you ca load it in the notebook file. The `load_listings()`  function takes the downloaded .csv.gz files and loads them into pandas DataFrames.

```bash 
airbnb-price-model/notebooks/01_airbnb_price_model.ipynb
```

All results in the notebook can be reproduced from scratch using these steps.

--- 


### Project Structure

airbnb-price-model/
├── data/
│   ├── raw/            # downloaded via script (ignored by git)
│   └── processed/
├── notebooks/
│   └── 01_airbnb_price_model.ipynb
├── src/
│   └── download_data.py
├── requirements.txt
└── README.md