### 📌 **Project Title**  
# 🛍️ Content-Based Product Recommendation System for E-Commerce  

## 📚 **Project Description**  
This project is a **Content-Based Product Recommendation System** built for an **E-Commerce platform**. The system recommends fashion products to users based on their search preferences, browsing history, and clicked categories.  

### **🔍 Key Features**  
👉 **Search-Based Recommendations**: Users can search for products, and the system retrieves relevant results.  
👉 **Category-Based Filtering**: Users can browse by categories like "For Men", "For Women", "For Boys", and "For Girls".  
👉 **User Interaction Logging**: Every click is logged to enhance personalized recommendations.  
👉 **Fast Query Processing**: Optimized data handling and UI updates ensure quick filtering and searching.  
👉 **Streamlit Web App Interface**: A clean and responsive UI built using **Streamlit**.  

---

## 📊 **Dataset Details**  

### **1️⃣ fashion_cleaned.csv**  
👉 **Contains structured product details like:**  
- `ProductID`: Unique identifier for each product  
- `ProductTitle`: Name of the fashion item  
- `Category`: Apparel, Footwear, Accessories, etc.  
- `Gender`: Men, Women, Boys, Girls  
- `ImageURL`: Link to the product image  
- `Price`: Product pricing  

### **2️⃣ user_interactions.csv**  
👉 **Logs user interactions for recommendations**  
- `timestamp`: When the user interacted  
- `user_id`: Tracks user behavior  
- `query`: The search term entered  
- `clicked_product`: The product the user clicked  

### **3️⃣ user_behavior_enhanced.csv**  
👉 **Enhances recommendation logic with user behavior analysis**  
- `user_id`: Identifies unique users  
- `action_type`: (e.g., Click, View, Add to Cart)  
- `session_duration`: Time spent on a product page  
- `recommendation_feedback`: Tracks user preferences  

---

## 💂 **Project Structure**  

```
📆 Content-Based Product Recommendation System
👉 data/
    👉 fashion_cleaned.csv  # Main dataset with product details
    👉 user_interactions.csv  # Logs user clicks and searches
    👉 user_behavior_enhanced.csv  # Tracks detailed user behavior
    👉 images/  # Contains product images

👉 notebooks/
    👉 recommendation_system_analysis.ipynb  # Jupyter Notebook for Data Analysis

👉 __pycache__/  # Auto-generated Python cache files
👉 app.py  # Streamlit Web App (Main File)
👉 fashion_ui.py  # UI Functions for Streamlit Interface
👉 Dockerfile  # Docker configuration for deployment
👉 requirements.txt  # List of required Python dependencies
👉 run_app.bat  # Windows script to start the Streamlit app
👉 README.md  # Project Documentation
```

---

## 🛠️ **How to Set Up & Run the Project Locally**  

### **1️⃣ Prerequisites**
Ensure you have the following installed:  
👉 **Python 3.8+**  
👉 **pip** (Python package manager)  
👉 **Streamlit**  

### **2️⃣ Clone the Repository**  
Run this command in your terminal or command prompt:  

```bash
git clone https://github.com/maheedhargowd/Content_based_Product_recommendation_System_E-Commerrce.git
cd Content_based_Product_recommendation_System_E-Commerrce
```

### **3️⃣ Create a Virtual Environment**  
#### **Windows**  
```bash
python -m venv venv
venv\Scripts\activate
```
#### **Mac/Linux**  
```bash
python3 -m venv venv
source venv/bin/activate
```

### **4️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **5️⃣ Run the Streamlit App**  
```bash
streamlit run app.py
```

👉 Open the **local URL** displayed in the terminal to view the web app.

---

## 🎮 **Project Functionalities & File Breakdown**

### **📝 app.py**  
- Main **Streamlit application**
- Loads datasets and initializes session states
- Handles **search queries and category-based filtering**
- Displays recommended products

### **🌟 fashion_ui.py**  
- Manages **UI components** (banner, category filters, search)
- Handles **product display layout**
- Connects user interactions with recommendation logic

### **📊 Notebooks (Data Analysis & Preprocessing)**  
- **recommendation_system_analysis.ipynb**: Jupyter notebook used for analyzing product similarity, TF-IDF scoring, and user interactions.

### **📂 Data Files**
- **fashion_cleaned.csv** → Contains **pre-processed product data**
- **user_interactions.csv** → Stores **logged user interactions** for tracking clicks/searches
- **user_behavior_enhanced.csv** → Advanced dataset for **detailed user analytics**

---

## 🚀 **Future Enhancements**
👉 Implement **Collaborative Filtering**  
👉 Integrate **Real-Time User Behavior Tracking**  
👉 Improve **Personalized Recommendations**  
👉 Add **Product Ratings & Reviews** for more refined suggestions  

---

## 🏆 **Contributing**
👉 **Want to improve this project?**  
Feel free to **fork this repo** and submit a **pull request**! 🎯  

---

## 💌 **Contact & Support**
📧 **Email**: maheedhargowd@gmail.com  
📌 **GitHub**: [@maheedhargowd](https://github.com/maheedhargowd)  

---

Let me know if you need any modifications or additions! 🚀

