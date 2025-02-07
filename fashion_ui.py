import streamlit as st

# ✅ Category Mapping to match dataset
CATEGORY_MAPPING = {
    "Women's": "Apparel",
    "Men's": "Apparel",
    "Accessories": "Footwear"
}

def show_banner():
    """Displays the main banner image."""
    st.image("data/images/banner2.jpg", use_container_width=True)

def show_categories():
    """Displays category selection buttons and updates recommendations."""
    st.subheader("📦 Shop by Category")

    categories = ["Women's", "Accessories", "Men's"]
    cols = st.columns(len(categories))

    for idx, category in enumerate(categories):
        if cols[idx].button(category):
            print(f"🛠️ Category Clicked: {category}")  # ✅ Debugging log

            st.session_state.selected_category = category  # ✅ Store Selected Category
            
            # ✅ Fetch Mapped Category
            mapped_category = CATEGORY_MAPPING.get(category, category)

            # ✅ Fetch Products with Mapped Category
            filtered_products = filter_products_by_category(mapped_category)
            st.session_state.recommendations = filtered_products  

            print(f"🔹 Mapped Category: {mapped_category}")
            print(f"🔹 Products Found: {len(filtered_products)} for {category}")

            st.rerun()  # ✅ Refresh UI

def filter_products_by_category(category):
    """Filters products based on category selection."""
    df_products = st.session_state.df_products  # ✅ Ensure product data is in session state
    
    print(f"✅ Available Categories in Data: {df_products['Category'].unique()}")  # Debugging
    
    filtered_products = df_products[df_products["Category"].str.lower().str.strip() == category.lower().strip()]

    print(f"🔹 Filtered Products for {category}: {filtered_products.shape[0]} items found.")  # Debugging

    return filtered_products
