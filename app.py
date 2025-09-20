import streamlit as st
import numpy as np
import pickle

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Student Performance Predictor", page_icon="🎓", layout="centered")

# 🌈 Custom CSS for teal & light blue background
page_bg = """
<style>
    .stApp {
        background: linear-gradient(to right, #008080, #87CEEB);
    }
    h1, h2, h3, h4, h5, h6, p {
        color: white;
    }
    .stButton>button {
        background-color: #006666;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #004C4C;
        color: #FFD700;
    }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Title
st.title("🎓 Student Performance Predictor")
st.markdown("Fill in the details below to predict a student's **Performance Index**.")

# Inputs
hours = st.number_input("📚 Hours Studied", min_value=0, max_value=24, value=5)
previous_score = st.number_input("📝 Previous Scores", min_value=0, max_value=100, value=70)
extracurricular = st.selectbox("🎭 Extracurricular Activities", ["Yes", "No"])
sleep = st.number_input("😴 Sleep Hours", min_value=0, max_value=24, value=7)
papers = st.number_input("📑 Sample Question Papers ", min_value=0, value=3)

# Encode categorical
extracurricular_num = 1 if extracurricular == "Yes" else 0

# Predict button
if st.button("🔮 Predict Performance Index"):
    features = np.array([[hours, previous_score, extracurricular_num, sleep, papers]])
    prediction = model.predict(features)[0]
    st.success(f"📈 Predicted Performance Index: **{prediction:.2f}**")
