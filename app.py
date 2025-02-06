import streamlit as st
import requests

# Hugging Face API URL
API_URL = "https://maheedhar97-product-recommendation-api.hf.space"  # Update if needed

# Streamlit UI
st.title("🛒 E-commerce Product Recommendation")

# Input for Product ID
product_id = st.text_input("Enter Product ID to get recommendations:")

if st.button("Get Recommendations"):
    if product_id:
        response = requests.get(f"{API_URL}/recommend/{product_id}")
        if response.status_code == 200:
            recommendations = response.json()
            st.subheader("Recommended Products:")
            for rec in recommendations:
                st.write(f"🔹 **{rec['ProductTitle']}** (ID: {rec['ProductId']})")
        else:
            st.error("Product ID not found!")
    else:
        st.warning("Please enter a valid Product ID!")
