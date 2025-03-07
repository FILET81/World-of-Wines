# Importing necessary libraries:
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.preprocessing import MinMaxScaler

# Importing dataset:
from WinesDatasetCleaning import wine_dataset_cleaning as wdc
wines_dataset = wdc()

# Dropping unnecessary columns:
wines_dataset.drop(columns=["country",
                            "apellation",
                            "taster_name",
                            "taster_twitter_handle",
                            "title",
                            "variety",
                            "winery",
                            "noble_international",
                            "monovarietal",
                            "taste_alcohol",
                            "primary_flavors",
                            "title_new"], inplace=True)

# Preparaing data for the model:
wines_filtered = wines_dataset[wines_dataset["price_usd"]<=75]

iqr_filtered = np.percentile(wines_filtered["vintage"], 75)-np.percentile(wines_filtered["vintage"], 25)
lower_limit_filtered = np.percentile(wines_filtered["vintage"], 25)-3*iqr_filtered

wines_predictor_filtered = wines_filtered[wines_filtered["vintage"] >= lower_limit_filtered]

# Defining the dependent variable:
y_v3 = wines_predictor_filtered["price_usd"]

# Defining the independent variables:
X_v3 = wines_predictor_filtered.drop(columns=["price_usd"])

X_num_v3 = X_v3.select_dtypes(np.number)
X_cat_v3 = X_v3.select_dtypes(object)

# Scaling "numerical" variables:
scaler_num_v3 = MinMaxScaler().fit_transform(X_num_v3)

# Getting dummies for "categorical" variables:
dummies_cat_v3 = pd.get_dummies(X_cat_v3, drop_first=True)

# Concatenating both "X_num" and "X_cat" variables:
X_v3 = np.concatenate((scaler_num_v3, dummies_cat_v3), axis=1)

# Splitting data between "train" and "test":
X_train, X_test, y_train, y_test = train_test_split(X_v3, y_v3, train_size=0.8, random_state=42)

# Defining the model:
rfr = RandomForestRegressor(n_estimators=500, max_depth=10, min_samples_leaf=4, random_state=42) 

# Fitting the model:
rfr.fit(X_train, y_train)

# Making predictions:
y_pred_rfr = rfr.predict(X_test)

# Evaluating performance of the model:
mse_rfr = mean_squared_error(y_test, y_pred_rfr)
r2_rfr = r2_score(y_test, y_pred_rfr)

# Printing the performance's results:
print("📘 Random Forest Regression:")
print(f"MSE (Mean Squared Error): {mse_rfr:.4f}")
print(f"R2 (Coefficient of Determination): {r2_rfr:.4f}")
