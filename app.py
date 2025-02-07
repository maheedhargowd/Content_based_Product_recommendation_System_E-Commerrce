import streamlit as st
import pandas as pd
import os
import datetime
import csv
import uuid
from fuzzywuzzy import fuzz, process
from sklearn.feature_extraction.text import TfidfVectorizer

from fashion_ui import show_banner, show_categories, filter_products_by_category

# ✅ Ensure Streamlit Config is First Command
st.set_page_config(page_title="Fashion Recommendation System", layout="wide")

# ✅ Page Title
st.title("👗 Welcome to Fashion Products Recommendation Page")

# ✅ Load Product Data and Store in Session State
if "df_products" not in st.session_state:
    df_products = pd.read_csv("data/fashion_cleaned.csv")
    df_products.fillna("", inplace=True)
    st.session_state.df_products = df_products  # ✅ Store Data in Session State

if "selected_category" not in st.session_state:
    st.session_state.selected_category = None
if "recommendations" not in st.session_state:
    st.session_state.recommendations = pd.DataFrame()

# ✅ Show Banner
show_banner()

# ✅ Show Category Buttons
show_categories()

# ✅ Display Recommended Products Based on Category Click
if st.session_state.selected_category:
    st.subheader(f"🛍️ {st.session_state.selected_category} Collection")
    
    if not st.session_state.recommendations.empty:
        rec_cols = st.columns(3)
        
        for r_idx, rec_product in st.session_state.recommendations.iterrows():
            with rec_cols[r_idx % 3]:
                if "ImageURL" in rec_product and rec_product["ImageURL"].strip():
                    st.image(rec_product["ImageURL"], width=200)
                else:
                    st.text("🚫 No Image Available")

                st.markdown(f"**{rec_product['ProductTitle']}**")
                st.text(f"Category: {rec_product['Category']}")
                st.text(f"Price: ${rec_product.get('Price', 'N/A')}")

    else:
        st.warning(f"⚠️ No products found for {st.session_state.selected_category}. Try another category.")



# **TF-IDF Vectorization for search**
tfidf_vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf_vectorizer.fit_transform(st.session_state.df_products["CleanedTitle"])

# **Function to log user interactions**
def log_user_interaction(user_id, query, clicked_product):
    """Log user interactions while preventing duplicate logging."""
    log_file = "data/user_interactions.csv"
    file_exists = os.path.exists(log_file)
    
    with open(log_file, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["timestamp", "user_id", "query", "clicked_product"])

        df_existing = pd.read_csv(log_file, dtype=str) if os.path.exists(log_file) else pd.DataFrame(columns=["timestamp", "user_id", "query", "clicked_product"])

        is_duplicate = (
            (df_existing["user_id"] == user_id) & 
            (df_existing["query"] == query) & 
            (df_existing["clicked_product"] == clicked_product)
        ).any()

        if not is_duplicate:
            writer.writerow([
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                user_id,
                query,
                clicked_product.replace(",", " ")
            ])

# **Function to search products based on query**
def search_products(query):
    """Perform fuzzy matching on product titles and categories."""
    query = query.lower()
    df_products = st.session_state.df_products  # ✅ Use session state data
    choices = df_products["ProductTitle"].astype(str).tolist() + df_products["Category"].astype(str).tolist()
    
    matches = process.extract(query, choices, limit=10, scorer=fuzz.partial_ratio)
    matched_products = [df_products[(df_products["ProductTitle"] == match[0]) | (df_products["Category"] == match[0])] for match in matches if match[1] > 60]

    return pd.concat(matched_products).drop_duplicates() if matched_products else pd.DataFrame()

# ✅ Search Bar
search_query = st.text_input("🔍 Search for a product, category, or keyword:", placeholder="Try 'men shorts', 'sports shoes', 'girl tops'...")

search_results = pd.DataFrame()
if search_query:
    search_results = search_products(search_query)
    
    if not search_results.empty:
        st.subheader(f"Search Results for '{search_query}'")
        cols = st.columns(3)

        for idx, product in search_results.iterrows():
            with cols[idx % 3]:
                st.image(product["ImageURL"], width=200)
                st.markdown(f"**{product['ProductTitle']}**")
                st.text(f"Category: {product['Category']}")
                st.text(f"Price: ${product.get('Price', 'N/A')}")

                button_key = f"view_{idx}_{uuid.uuid4().hex}"
                if st.button(f"View {product['ProductTitle']}", key=button_key):
                    log_user_interaction("guest", search_query, product['ProductTitle'])
                    st.session_state.selected_product = product['ProductTitle']
                    st.session_state.recommendations = filter_products_by_category(product["Category"])  # ✅ Fetch recommendations
                    st.rerun()  # ✅ Refresh UI
