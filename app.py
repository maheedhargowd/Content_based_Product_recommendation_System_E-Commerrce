import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

# Load dataset
df_products = pd.read_csv("data/fashion_cleaned.csv")




# # 🔍 Debugging: Print column names
# st.write("Columns in df_products:", list(df_products.columns))

# Combine relevant columns for better search (Title, Category, Description, Keywords)
df_products["combined_text"] = (
    df_products["ProductTitle"].fillna("") + " " +
    df_products["Category"].fillna("") + " " +
    df_products["SubCategory"].fillna("")
)
df_products["SearchableText"] = (
    df_products["ProductTitle"].fillna("") + " " +
    df_products["Category"].fillna("") + " " +
    df_products["SubCategory"].fillna("")
)

# TF-IDF Vectorizer to improve search
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df_products["combined_text"])

# Function to improve search using text similarity
def search_products(query, top_n=6):
    query_vector = vectorizer.transform([query])
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix).flatten()
    
    top_indices = similarity_scores.argsort()[-top_n:][::-1]
    return df_products.iloc[top_indices]

# Display product in a card-like structure
def display_product(product):
    with st.container():
        st.image(product["ImageURL"], width=200)
        st.write(f"**{product['ProductTitle']}**")
        st.caption(f"Category: {product['Category']}")
        st.caption(f"Price: ${product.get('Price', 'N/A')}")
        st.write("------")

# Main UI
st.title("🛍️ Fashion Recommendation System")
st.markdown("🔍 *Search for a product, category, or keyword:*")

# Search bar
search_query = st.text_input("Enter product name or keyword:", "")

if search_query:
    st.subheader(f"🔎 Search Results for '{search_query}'")
    results = search_products(search_query)
    
    if results.empty:
        st.warning("❌ No matching products found. Try different keywords.")
    else:
        # Display products in rows of 3
        cols = st.columns(3)
        for i, (_, product) in enumerate(results.iterrows()):
            with cols[i % 3]:
                display_product(product)
