import streamlit as st

def show_banner():
    st.image("data/images/banner2.jpg", use_container_width=True)

def show_categories(df_products, reset_search_callback):
    st.subheader("🛍️ Shop by Category", divider="gray")
    
    categories = ["Men", "Women", "Boys", "Girls"]
    
    # Align categories horizontally using `columns`
    cols = st.columns(len(categories))
    for idx, category in enumerate(categories):
        if cols[idx].button(category):
            st.session_state.selected_category = category.lower()
            reset_search_callback()  # Reset search results when a category is clicked

    st.markdown(f"### 📊 Filtering for category: **{st.session_state.selected_category.capitalize() if st.session_state.selected_category else 'None'}**")

def display_products_grid(products):
    """Display products in a 4-column layout."""
    cols = st.columns(4)  # Creating 4 columns for grid layout
    for idx, (_, row) in enumerate(products.iterrows()):
        with cols[idx % 4]:  # Place images in 4 columns per row
            st.image(row["ImageURL"], caption=row["ProductTitle"], width=180)
