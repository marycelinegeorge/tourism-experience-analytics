# 🌍 Tourism Experience Analytics System

An end-to-end **Machine Learning–based Tourism Analytics application** that analyzes user travel behavior, predicts visit modes, recommends attractions, and visualizes tourism insights using real-world data.

🚀 **Live App**: https://tourism-analytics-2026.streamlit.app  
📦 **GitHub Repo**: https://github.com/marycelinegeorge/tourism-experience-analytics

---

## 📌 Project Overview

This project was built as part of an **internship assignment** to demonstrate the complete ML lifecycle:
- Data preprocessing and feature engineering
- Exploratory Data Analysis (EDA)
- Model training (offline)
- Recommendation logic
- Interactive deployment using **Streamlit Cloud**

The deployed app gracefully runs in **Demo Mode** when trained models are not loaded, following best ML engineering practices.

---

## 🧠 Problem Statement

Tourism platforms generate large volumes of user interaction data.  
The goal of this project is to:
- Understand user travel preferences
- Predict **Visit Mode** (e.g., Family, Business, Solo)
- Recommend attractions based on ratings and preferences
- Provide actionable tourism insights through visualizations

---

## 🗂️ Dataset Description

The final consolidated dataset was created by merging multiple relational tables:

- `transactions`
- `users`
- `cities`
- `countries`
- `regions`
- `continents`
- `visit_modes`
- `attraction_types`
- `items`

📁 Processed dataset used in deployment:
## data/processed/final_dataset.csv

Key features include:
- User demographics (continent, country, region)
- Attraction details and types
- Visit mode
- Scaled ratings (`Rating_scaled`)

---

## 🔧 Data Processing & Feature Engineering

- Handled missing values and invalid entries
- Encoded categorical variables
- Aggregated user-level features
- Scaled numerical features (ratings)
- Created a clean, analytics-ready dataset

---

## 📊 Exploratory Data Analysis (EDA)

Integrated directly into the app:
- Attraction Type Distribution
- Region-wise User Distribution
- Rating-based attraction popularity

---

## 🤖 Machine Learning (Offline)

### Models trained locally:
- **Classification**: Predict Visit Mode
- **Regression**: Predict User Ratings
- **Recommendation**: Content-based filtering using attraction ratings

> ⚠️ Model `.pkl` files are **not included in deployment** to:
> - Avoid large file uploads
> - Follow secure & scalable ML deployment practices

The app automatically switches to **Demo Mode** if models are unavailable.

---

## 🎯 Application Features

### 🔮 Visit Mode Prediction
- Predicts preferred visit mode based on user inputs
- Shows demo output when models are not loaded

### 🎯 Attraction Recommendations
- Top attractions by `AttractionType`
- Ranked using mean `Rating_scaled`

### 📊 Tourism Insights
- Interactive charts for attraction types and regions

---

## 🖥️ Tech Stack

- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Streamlit**
- **Joblib**
- **Git & GitHub**
- **Streamlit Cloud**

---

## 🚀 Deployment

The application is deployed using **Streamlit Cloud**.

Deployment flow:
1. Push clean code to GitHub
2. Configure Streamlit Cloud with:
   - `main` branch
   - `app.py` entry point
3. Automatic CI/CD on every commit

---

## 📂 Project Structure
### tourism-experience-analytics/
## │
## ├── app.py # Streamlit application
## ├── requirements.txt # Dependencies
## ├── data/
## │ └── processed/
## │ └── final_dataset.csv
## ├── notebooks/
## │ └── Tourism_Experience_Analytics_MARY_CELINE.ipynb
## ├── models/ # (Ignored in deployment)
## ├── .gitignore
## └── README.md

---

## 🧑‍💼 Author

**Mary Celine George**  
Aspiring Data Scientist | ML Engineer  
📍 India

---

## 📌 Key Takeaways

- Demonstrates full ML pipeline
- Clean, production-ready deployment
- Handles missing models gracefully
- Interview and internship ready

---

⭐ *If you like this project, feel free to star the repo!*  