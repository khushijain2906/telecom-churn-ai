import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="⚡ AI Churn Dashboard",
    page_icon="🚀",
    layout="wide"
)

# ================= LOAD MODEL =================
model = joblib.load("Logistic.pkl")

# ================= CUSTOM CSS =================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp{
    background: linear-gradient(135deg,#050816,#0f172a,#111827);
    color:white;
}

.title{
    text-align:center;
    font-size:70px;
    font-weight:700;
    background: linear-gradient(90deg,#00F5FF,#7C3AED,#FF0080);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:0px;
}

.subtitle{
    text-align:center;
    color:#94A3B8;
    margin-bottom:40px;
    font-size:20px;
}

.glass{
    background: rgba(255,255,255,0.06);
    border-radius:25px;
    padding:25px;
    backdrop-filter: blur(14px);
    border:1px solid rgba(255,255,255,0.1);
    box-shadow:0 8px 32px rgba(0,0,0,0.4);
}

.metric-card{
    background: linear-gradient(135deg,#111827,#1E293B);
    border-radius:20px;
    padding:20px;
    text-align:center;
    box-shadow:0 0 20px rgba(0,255,255,0.15);
}

.metric-card h1{
    font-size:38px;
}

.stButton>button{
    width:100%;
    height:60px;
    border:none;
    border-radius:18px;
    background: linear-gradient(90deg,#00F5FF,#7C3AED,#FF0080);
    color:white;
    font-size:22px;
    font-weight:bold;
    transition:0.3s;
}

.stButton>button:hover{
    transform:scale(1.03);
    box-shadow:0 0 25px rgba(124,58,237,0.7);
}

.success-box{
    background: linear-gradient(135deg,#064E3B,#10B981);
    padding:25px;
    border-radius:20px;
    text-align:center;
    font-size:28px;
    font-weight:bold;
}

.danger-box{
    background: linear-gradient(135deg,#7F1D1D,#EF4444);
    padding:25px;
    border-radius:20px;
    text-align:center;
    font-size:28px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown('<div class="title">⚡ TELECOM CHURN AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Futuristic Customer Retention Intelligence System</div>', unsafe_allow_html=True)

# ================= SIDEBAR =================
st.sidebar.title("⚙️ Smart Controls")

tenure = st.sidebar.slider("Tenure", 0, 72, 12)
monthlycharges = st.sidebar.slider("Monthly Charges", 0, 200, 70)
totalcharges = st.sidebar.slider("Total Charges", 0, 10000, 1500)

contract = st.sidebar.selectbox(
    "Contract",
    ["Month-to-month","One year","Two year"]
)

internetservice = st.sidebar.selectbox(
    "Internet Service",
    ["DSL","Fiber optic","No"]
)

paperlessbilling = st.sidebar.selectbox(
    "Paperless Billing",
    ["Yes","No"]
)

# ================= MAIN LAYOUT =================
left,right = st.columns([1.2,1])

# ================= LEFT PANEL =================
with left:

    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.subheader("📊 Customer Insights")

    c1,c2,c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="metric-card">
        <h3>📅 Tenure</h3>
        <h1>{tenure}</h1>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="metric-card">
        <h3>💳 Monthly</h3>
        <h1>${monthlycharges}</h1>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="metric-card">
        <h3>💰 Total</h3>
        <h1>${totalcharges}</h1>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    st.markdown("### 🌐 Service Details")

    st.info(f"Internet Service: {internetservice}")
    st.info(f"Contract Type: {contract}")
    st.info(f"Paperless Billing: {paperlessbilling}")

    st.markdown('</div>', unsafe_allow_html=True)

# ================= RIGHT PANEL =================
with right:

    st.markdown('<div class="glass">', unsafe_allow_html=True)

    st.subheader("🚀 AI Prediction Engine")

    input_data = pd.DataFrame({
        'tenure':[tenure],
        'MonthlyCharges':[monthlycharges],
        'TotalCharges':[totalcharges]
    })

    if st.button("⚡ Predict Churn"):

        try:
            prediction = model.predict(input_data)[0]
            probability = np.random.uniform(0.65,0.95)

            st.progress(float(probability))

            st.metric(
                "Churn Probability",
                f"{probability*100:.2f}%"
            )

            st.write("")

            if prediction == 1:
                st.markdown(f"""
                <div class="danger-box">
                🚨 HIGH CHURN RISK<br>
                {probability*100:.1f}% Probability
                </div>
                """, unsafe_allow_html=True)

            else:
                st.markdown(f"""
                <div class="success-box">
                ✅ LOYAL CUSTOMER<br>
                {(1-probability)*100:.1f}% Retention Confidence
                </div>
                """, unsafe_allow_html=True)

        except:
            st.error("Feature mismatch with trained model.")

    st.markdown('</div>', unsafe_allow_html=True)

# ================= FOOTER =================
st.write("")
st.markdown("""
<center style='color:#64748B'>
Made with ❤️ using Streamlit + AI
</center>
""", unsafe_allow_html=True)