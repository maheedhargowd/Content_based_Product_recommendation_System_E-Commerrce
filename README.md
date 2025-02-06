#  Content-Based Product Recommendation System

## 🔍 Overview
This project is a **content-based recommendation system** for an e-commerce platform, built using **FastAPI, Streamlit, and machine learning techniques**. It helps users find **fashion products** based on textual descriptions, categories, and product similarities.

The system uses **TF-IDF and cosine similarity** for text-based recommendations and integrates **fuzzy matching** for enhanced search accuracy.

🔗 **Live Demo:** [Hugging Face Space](https://huggingface.co/spaces/maheedhar97/product-recommendation-api)

---

## 📂 Project Structure
## 📓 Jupyter Notebook
The data preprocessing and recommendation system analysis is available in [this notebook](notebooks/product_recommendation.ipynb).

### 📚 `data/` - Dataset & Precomputed Similarity Files
- `fashion_cleaned.csv` → Preprocessed product data
- `final_similarity.npy` → Combined similarity scores
- `image_features.pkl` → Image-based feature extraction
- `image_similarity.npy` → Image-based similarity matrix
- `text_similarity.npy` → Text-based similarity matrix
- `tfidf_matrix.pkl` → TF-IDF vectorized matrix
- `tfidf_similarity.pkl` → TF-IDF-based similarity scores
- `user_behavior_enhanced.csv` → User behavior dataset (optional)

### 📌 Other Important Files
- **`app.py`** → Streamlit UI for user interaction
- **`main.py`** → FastAPI backend for API endpoints
- **`requirements.txt`** → Dependencies for the project
- **`Dockerfile`** → Docker setup for deployment
- **`run_app.bat`** → Windows batch file to run the app
- **`README.md`** → Project documentation (this file)

---

## 🚀 Installation & Setup

### 🔹 1. Clone the Repository
```sh
git clone https://github.com/maheedhargowd/Content_based_Product_recommendation_System_E-Commerrce.git
cd Content_based_Product_recommendation_System_E-Commerrce
```

### 🔹 2. Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
```
Activate it:
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### 🔹 3. Install Dependencies
```sh
pip install -r requirements.txt
```

---

## 🎯 Running the Project

### ✅ **1. Start the API Backend (FastAPI)**
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
- This will launch the FastAPI server at **http://127.0.0.1:8000**.
- You can access the API docs at: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**.

### ✅ **2. Start the Streamlit Frontend**
```sh
streamlit run app.py
```
- This will launch the **Streamlit UI** for product search.

---

## 📌 Features

🔄 **TF-IDF & Cosine Similarity** – Finds products with similar textual descriptions.  
🌟 **Fuzzy Matching** – Enhances search results for misspelled words or partial matches.  
🎨 **Image-Based Similarity** – Uses precomputed image embeddings for recommendations.  
👨‍💻 **User Interaction** – Streamlit-powered UI for an easy search experience.  
🌐 **Deployed on Hugging Face** – Live demo available online.  

---

## 🎡 Deployment (Hugging Face)
This project is **deployed on Hugging Face Spaces**. You can access it [here](https://huggingface.co/spaces/maheedhar97/product-recommendation-api).  
To deploy yourself:
```sh
git add .
git commit -m "Updated version"
git push
```
Your Hugging Face Space should automatically update.

---

## 🤝 Contributions
Contributions are welcome! Feel free to submit a **Pull Request** or open an **Issue**.

---

## 📚 License
This project is open-source and available under the **MIT License**.

