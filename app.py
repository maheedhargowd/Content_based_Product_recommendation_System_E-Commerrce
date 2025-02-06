import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz, process




# Load dataset
df_products = pd.read_csv("data/fashion_cleaned.csv")

# Fill missing values
df_products.fillna("", inplace=True)

# Precompute TF-IDF Matrix for search
tfidf_vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf_vectorizer.fit_transform(df_products["CleanedTitle"])  # Use Cleaned Title for search


def search_products(query, df_products):
    """
    Perform fuzzy matching on product titles and categories to improve search accuracy.
    """
    query = query.lower()
    
    # Extract titles and categories
    choices = df_products["ProductTitle"].astype(str).tolist() + df_products["Category"].astype(str).tolist()
    
    # Get the best matches
    matches = process.extract(query, choices, limit=10, scorer=fuzz.partial_ratio)
    
    # Retrieve matching product details
    matched_products = []
    for match, score in matches:
        if score > 60:  # Adjust this threshold based on testing
            product = df_products[(df_products["ProductTitle"] == match) | (df_products["Category"] == match)]
            matched_products.append(product)

    return pd.concat(matched_products).drop_duplicates() if matched_products else pd.DataFrame()


# Function to handle fuzzy matching
def fuzzy_search(query):
    product_titles = df_products["CleanedTitle"].tolist()
    best_match, confidence = process.extractOne(query, product_titles)
    
    if confidence > 75:  # If confidence is high, return the best matching product
        return df_products[df_products["CleanedTitle"] == best_match].iloc[0]
    return None

# Streamlit UI
st.set_page_config(page_title="Fashion Recommendation System", layout="wide")

st.title("🛍️ Fashion Recommendation System")
st.markdown("**Search for a product, category, or keyword:**")

search_query = st.text_input("Enter product name or keyword:")

if search_query:
    search_results = search_products(search_query, df_products)
    
    if not search_results.empty:

        st.subheader(f" Search Results for '{search_query}'")
        cols = st.columns(3)  # Display results in 3 columns
        
        for idx, product in search_results.iterrows():

            with cols[idx % 3]:  # Arrange in grid layout
                st.image(product["ImageURL"], width=200)
                st.markdown(f"**{product['ProductTitle']}**")
                st.text(f"Category: {product['Category']}")
                st.text(f"Price: ${product.get('Price', 'N/A')}")
    
    else:
        fuzzy_match = fuzzy_search(search_query)
        
        if fuzzy_match is not None:
            st.warning(f"Did you mean: **{fuzzy_match['ProductTitle']}**?")
        else:
            st.error("❌ No matching products found. Try different keywords.")
