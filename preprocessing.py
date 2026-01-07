import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
import pickle

# Load dataset
url = "https://drive.google.com/uc?export=download&id=1oFn9nfrL1sx2XvRBwysffu66waHX7Sm4"
df = pd.read_csv(url)

# Drop duplicates and rows with missing values
df.drop_duplicates(inplace=True)
df.dropna(subset=['name', 'city', 'cuisine', 'cost', 'rating'], inplace=True)

# Clean 'cost' column ('₹ 200' -> 200)
df['cost'] = df['cost'].astype(str).str.replace('₹', '', regex=False).str.replace(',', '', regex=False).str.strip()
df['cost'] = pd.to_numeric(df['cost'], errors='coerce')

# Ensure rating is numeric
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# Drop rows with invalid 'cost' or 'rating'
df.dropna(subset=['cost', 'rating'], inplace=True)

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)
print("✅ cleaned_data.csv saved")

# One Hot Encoding
encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
encoded_data = encoder.fit_transform(df[['city', 'cuisine']])

# Convert to DataFrame with correct column names
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(['city', 'cuisine']))

# Reset indices
encoded_df.reset_index(drop=True, inplace=True)
df.reset_index(drop=True, inplace=True)

# Add the numerical columns (cost and rating)
encoded_df['cost'] = df['cost']
encoded_df['rating'] = df['rating']

# Save the encoded dataset
encoded_df.to_csv("encoded_data.csv", index=False)
print("✅ encoded_data.csv saved")

# Save encoder to pickle
with open("encoder.pkl", "wb") as f:
    pickle.dump(encoder, f)
print("✅ encoder.pkl saved")

