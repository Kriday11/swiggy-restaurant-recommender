import streamlit as st
import pandas as pd
import pickle
from recommendation import get_recommendations

# Load the encoder and cleaned data
with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

# Title of the web app
st.title("Swiggy Restaurant Recommendation System")

# User input for city, cuisine, cost, and rating
city = st.selectbox("Select City", ['Bangalore', 'Mumbai', 'Delhi', 'Chennai', 'Kolkata'])
cuisine = st.selectbox("Select Cuisine", ['North Indian', 'South Indian', 'Chinese', 'Italian', 'Mexican'])
cost = st.slider("Select Cost", 100, 1000, 200)  # Min = 100, Max = 1000, Default = 200
rating = st.slider("Select Rating", 1.0, 5.0, 4.0)  # Min = 1, Max = 5, Default = 4

# Button to get recommendations
if st.button("Get Recommendations"):
    # Fetch recommendations using the provided input
    recommendations = get_recommendations(city, cuisine, cost, rating, top_n=5)

    # Display results in a table
    st.subheader("Top 5 Restaurant Recommendations:")
    st.write(recommendations)
