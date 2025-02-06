from fastapi import FastAPI
import pandas as pd
import numpy as np
import pickle

app = FastAPI()

# Load product data
df_products = pd.read_csv("data/fashion_cleaned.csv")
product_ids = df_products["ProductId"].values

# Load final similarity matrix
final_similarity = np.load("data/final_similarity.npy")

# Recommendation function
def recommend_products(product_id, top_n=5):
    if product_id not in product_ids:
        return {"error": "Product ID not found!"}
    
    idx = np.where(product_ids == product_id)[0][0]
    similarity_scores = final_similarity[idx]
    similar_indices = np.argsort(similarity_scores)[::-1][1:top_n+1]
    
    recommended_items = df_products.iloc[similar_indices][["ProductId", "ProductTitle"]].to_dict(orient="records")
    return recommended_items

# Define API endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the Product Recommendation API!"}

@app.get("/recommend/{product_id}")
def get_recommendations(product_id: int, top_n: int = 5):
    recommendations = recommend_products(product_id, top_n)
    return {"Product ID": product_id, "Recommendations": recommendations}
