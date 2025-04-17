# Importing necessary libraries:
import numpy as np
import pandas as pd
from WinesDatasetCleaning import wine_dataset_cleaning as wdc
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
import pickle

# Loading and preparing the dataset:
wines_dataset = wdc()

# Applying dataset restrictions:
p_filter = 75
wines_filtered = wines_dataset[wines_dataset["price_usd"] <= p_filter]
iqr_filtered = np.percentile(wines_filtered["vintage"], 75) - np.percentile(wines_filtered["vintage"], 25)
lower_limit_filtered = np.percentile(wines_filtered["vintage"], 25) - 3 * iqr_filtered

wines_predictor_filtered = wines_filtered[wines_filtered["vintage"] >= lower_limit_filtered]

# Selecting necessary columns:
data = wines_predictor_filtered[["price_usd", "points", "wine_type", "avg_abv_%", "avg_serve_temp_c",
                                 "taste_dry-sweet", "taste_body", "taste_tannins", "taste_acidity", "vintage"]]

# Defining dependent (y) and independent (Xs) variables:
y = data["price_usd"]
X = data.drop(columns=["price_usd"])

# Splitting into numerical and categorical data:
X_num = X.select_dtypes(np.number)
X_cat = X.select_dtypes(object)

# Scaling numerical features:
scaler = MinMaxScaler().fit(X_num)
X_num_scaled = scaler.transform(X_num)

# Encoding categorical features:
X_cat_dummies = pd.get_dummies(X_cat, drop_first=True)

# Combining features:
X_final = np.concatenate((X_num_scaled, X_cat_dummies), axis=1)

# Training the model:
model = RandomForestRegressor(n_estimators=500, max_depth=10, min_samples_leaf=4, random_state=42)
model.fit(X_final, y)

# Saving the model and preprocessing tools:
with open("wine_model.pkl", "wb") as pprfr:
    pickle.dump({
        "model": model,
        "scaler": scaler,
        "cat_columns": X_cat_dummies.columns,
        "features": X.columns,
        "mode_vintage": int(data["vintage"].mode()[0])     # Helpful for the reuse in UI!!!
        }, pprfr)