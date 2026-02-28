import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Tourism Experience Analytics", layout="wide")

st.title("🌍 Tourism Experience Analytics")

# Load assets
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/final_dataset.csv")

@st.cache_resource
def load_models():
    clf = joblib.load("models/visit_mode_classifier.pkl")
    reg = joblib.load("models/rating_regressor.pkl")
    return clf, reg

df = load_data()
clf_model, reg_model = load_models()

# Sidebar inputs
st.sidebar.header("User Preferences")

continent = st.sidebar.selectbox("Continent", df["Continent"].unique())
country = st.sidebar.selectbox("Country", df["Country"].unique())
attraction_type = st.sidebar.selectbox("Attraction Type", df["AttractionType"].unique())

# Prediction
if st.sidebar.button("Predict Visit Mode"):
    sample = df.iloc[[0]].copy()
    sample["Continent"] = continent
    sample["Country"] = country
    pred = clf_model.predict(sample)[0]
    st.success(f"Predicted Visit Mode: {pred}")

# Recommendations
st.subheader("🎯 Recommended Attractions")

top_attractions = (
    df[df["AttractionType"] == attraction_type]
    .groupby("Attraction")["Rating"]
    .mean()
    .sort_values(ascending=False)
    .head(5)
)

st.table(top_attractions.reset_index())

# Visuals
st.subheader("📊 Tourism Insights")

col1, col2 = st.columns(2)

with col1:
    st.bar_chart(df["AttractionType"].value_counts())

with col2:
    st.bar_chart(df["Region"].value_counts())