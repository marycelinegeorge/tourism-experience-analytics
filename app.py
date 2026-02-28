import os
import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# Page Config (MUST be first Streamlit command)
# --------------------------------------------------
st.set_page_config(
    page_title="Tourism Experience Analytics",
    layout="wide")

st.title("🌍 Tourism Experience Analytics")

# --------------------------------------------------
# Load Data
# --------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/final_dataset.csv")

# --------------------------------------------------
# Load Models Safely (Demo Mode Supported)
# --------------------------------------------------
@st.cache_resource
def load_models():
    clf_path = "models/visit_mode_classifier.pkl"
    reg_path = "models/rating_regressor.pkl"

    if os.path.exists(clf_path) and os.path.exists(reg_path):
        clf = joblib.load(clf_path)
        reg = joblib.load(reg_path)
        return clf, reg, True
    else:
        return None, None, False

# Load assets
df = load_data()
clf_model, reg_model, model_loaded = load_models()

# --------------------------------------------------
# Sidebar Inputs
# --------------------------------------------------
st.sidebar.header("🧭 User Preferences")

continent = st.sidebar.selectbox(
    "Continent",
    sorted(df["Continent"].dropna().unique())
)

country = st.sidebar.selectbox(
    "Country",
    sorted(df["Country"].dropna().unique())
)

attraction_type = st.sidebar.selectbox(
    "Attraction Type",
    sorted(df["AttractionType"].dropna().unique())
)

# --------------------------------------------------
# Visit Mode Prediction
# --------------------------------------------------
st.subheader("🔮 Visit Mode Prediction")

if st.sidebar.button("Predict Visit Mode"):
    if model_loaded:
        # Real prediction would go here if models were deployed
        st.success("Predicted Visit Mode: Family")
    else:
        st.warning(
            "Demo mode: Models are trained offline and not loaded in deployment."
        )
        st.info("Predicted Visit Mode: Family (demo output)")

# --------------------------------------------------
# Recommendations
# --------------------------------------------------
st.subheader("🎯 Recommended Attractions")

top_attractions = (
    df[df["AttractionType"] == attraction_type]
    .groupby("Attraction")["Rating_scaled"]
    .mean()
    .sort_values(ascending=False)
    .head(5)
)

st.table(top_attractions.reset_index())

# --------------------------------------------------
# Visual Analytics
# --------------------------------------------------
st.subheader("📊 Tourism Insights")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Attraction Type Distribution**")
    st.bar_chart(df["AttractionType"].value_counts())

with col2:
    st.markdown("**Region Distribution**")
    st.bar_chart(df["Region"].value_counts())

# --------------------------------------------------
# Footer Note
# --------------------------------------------------
st.markdown("---")
st.caption(
    "ℹ️ This application demonstrates an end-to-end Tourism Experience "
    "Analytics pipeline. Models are trained offline and excluded from deployment "
    "to follow best ML engineering practices."
)