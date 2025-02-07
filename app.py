import streamlit as st
import pandas as pd
from fashion_ui import show_banner, show_categories, display_products_grid

# Set up Streamlit page
st.set_page_config(page_title="Fashion Recommendation", layout="wide")

# Load product dataset into session state if not already loaded
if "df_products" not in st.session_state:
    st.session_state.df_products = pd.read_csv("data/fashion_cleaned.csv")

if "selected_category" not in st.session_state:
    st.session_state.selected_category = None

if "search_query" not in st.session_state:
    st.session_state.search_query = ""

# Function to reset search query when category is clicked
def reset_search():
    st.session_state["search_query"] = ""


# Add App Title
st.markdown(
    "<h1 style='text-align: center; color: #FF4081;'>🛍️ AI-Powered Fashion Discovery</h1>", 
    unsafe_allow_html=True
)


# Display Banner
show_banner()

# Search Bar - Always Visible
query = st.text_input("🔍 Search for a product, category, or keyword:", 
                      placeholder="Try 'men shorts', 'sports shoes', 'girl tops'...",
                      value=st.session_state.search_query,
                      key="search_input")  # Use a different key to avoid conflict

# Update session state search query only if the user types something
if query != st.session_state.search_query:
    st.session_state.search_query = query

# Show Categories (Now Horizontal) and Reset Search on Category Selection
show_categories(st.session_state.df_products, reset_search)

# If a search query exists, show search results and do not filter by category
if st.session_state.search_query.strip():  
    st.markdown(f"## 🔎 Search Results for '{st.session_state.search_query}'")
    search_results = st.session_state.df_products[
        st.session_state.df_products["ProductTitle"].str.contains(st.session_state.search_query, case=False, na=False)
    ]
    if not search_results.empty:
        display_products_grid(search_results.head(30))  # Display search results
    else:
        st.warning(f"No results found for '{st.session_state.search_query}'.")
else:
    # If no search query, show category-based filtering
    if st.session_state.selected_category:
        filtered_products = st.session_state.df_products[
            st.session_state.df_products['Gender'].str.lower() == st.session_state.selected_category.lower()
        ]

        st.markdown(f"## 🛍️ {st.session_state.selected_category.capitalize()} Collection")
        st.markdown(f"### 📊 Total Products: {len(filtered_products)}")

        if not filtered_products.empty:
            display_products_grid(filtered_products.head(30))  # Display filtered products
        else:
            st.warning(f"No products found under '{st.session_state.selected_category}'. Try another category.")
