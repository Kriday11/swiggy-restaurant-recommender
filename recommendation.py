import pandas as pd
import numpy as np
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Load encoded data
encoded_df = pd.read_csv("encoded_data.csv")

# Load cleaned data
cleaned_df = pd.read_csv("cleaned_data.csv")

# Load encoder
with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

# Recommendation function
def get_recommendations(city, cuisine, cost, rating, top_n=5):
    # Create a DataFrame with the user's input
    input_dict = {'city': [city], 'cuisine': [cuisine]}
    
    # One-hot encode the input
    input_encoded = encoder.transform(pd.DataFrame(input_dict))
    input_encoded_df = pd.DataFrame(input_encoded, columns=encoder.get_feature_names_out(['city', 'cuisine']))

    # Add cost and rating
    input_encoded_df['cost'] = cost
    input_encoded_df['rating'] = rating

    # Make sure input and dataset columns match
    input_encoded_df = input_encoded_df.reindex(columns=encoded_df.columns, fill_value=0)

    # Compute cosine similarity
    similarity = cosine_similarity(input_encoded_df, encoded_df)

    # Get indices of top matches
    top_indices = similarity[0].argsort()[::-1][:top_n]

    # Fetch restaurant details from cleaned_df
    return cleaned_df.iloc[top_indices][['name', 'city', 'cuisine', 'cost', 'rating']]

# -------- Test the function (optional) --------
if __name__ == "__main__":
    city = "Bangalore"
    cuisine = "North Indian"
    cost = 300
    rating = 4.2

    recommendations = get_recommendations(city, cuisine, cost, rating, top_n=5)
    print("Top Recommendations:")
    print(recommendations)
