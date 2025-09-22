import streamlit as st  
import numpy as np
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Student Performance Predictor", page_icon="🎓", layout="centered")

#***CSS***

page_style = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background-color: #cce0ff;  
    }

    .hero {
        text-align: center;
        padding: 40px;
        border-radius: 16px;
        background: linear-gradient(135deg, #36d1dc, #5b86e5);
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        opacity: 0;
        transform: translateY(20px);
        animation: fadeInUp 1s forwards;
    }

    .card {
        background: white;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        transition: transform 0.2s ease-in-out;
    }
    .card:hover {
        transform: translateY(-5px);
    }

    .result-box {
        padding: 20px;
        border-radius: 16px;
        background: linear-gradient(135deg, #4facfe, #00f2fe);
        color: white;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        opacity: 0;
        transform: translateY(20px);
        animation: fadeInUp 1s forwards;
    }

    .stButton>button {
        background-color: #5b86e5;
        color: white;
        border-radius: 12px;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    .stButton>button:hover {
        background-color: #36d1dc;
        color: #fff;
    }

    [data-testid="stMarkdownContainer"] h2,
    div[role="heading"][aria-level="2"] {
      color: #111111 !important;
      font-size: 22px !important;
      font-weight: 700 !important;
    } 

    label, .stExpander p, .stExpander ul, .stExpander li {
        color: #212121 !important;
        font-size: 18px !important;
        font-weight: 600;
    }

    .stExpander li:hover {
        background-color: #f0f0f0;
        border-radius: 6px;
        padding: 4px 6px;
        transition: background-color 0.2s ease-in-out;
        cursor: pointer;
    }

    @keyframes fadeInUp {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)


st.markdown("""
<div class="hero">
    <h1>🎓 Student Performance Predictor</h1>
    <p>
        Discover how your study habits, sleep, and activities influence your academic performance.  
        Enter your details below and get both predictions and tips for improvement.
    </p>
</div>
""", unsafe_allow_html=True)

#***input form*** 

st.subheader("📌 Enter Your Details")

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    hours = st.number_input("📚 Hours Studied", min_value=0, max_value=24, value=5)
    previous_score = st.number_input("📝 Previous Scores", min_value=0, max_value=100, value=70)
    extracurricular = st.selectbox("🎭 Extracurricular Activities", ["Yes", "No"])
    sleep = st.slider("😴 Sleep Hours", 0, 12, 7)
    papers = st.number_input("📑 Sample Question Papers", min_value=0, value=3)
    st.markdown('</div>', unsafe_allow_html=True)

extracurricular_num = 1 if extracurricular == "Yes" else 0

#***prediction***

if st.button("Predict Performance Index"):
    features = np.array([[hours, previous_score, extracurricular_num, sleep, papers]])
    prediction = model.predict(features)[0]

    st.markdown(f"<div class='result-box'>📈 Predicted Performance Index: <b>{prediction:.2f}</b></div>", unsafe_allow_html=True)

    if prediction < 60:
        with st.expander("💡 Tips to Improve Your Score"):
            st.markdown("""
            -  Increase your study hours gradually.  
            -  Solve more past exam papers.  
            -  Maintain a regular sleep schedule.  
            -  Balance activities with study time.  
            -  Revise weak topics more often.  
            """)
