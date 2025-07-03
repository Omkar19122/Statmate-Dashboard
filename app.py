
import streamlit as st
from PIL import Image

logo = Image.open("statmate_logo.png")

col1, col2 = st.columns([1, 4])
with col1:
    st.image(logo, width=60)
with col2:
    st.title("STATMATE")
    st.caption("Clinical Trial & Patient Data Insights")

st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Analysis", "Help"])
language = st.sidebar.selectbox("Language", ["English", "Marathi"])

with st.sidebar.expander("🔐 Login"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.success(f"Welcome, {username}!")

if page == "Home":
    st.subheader("Statmate मध्ये स्वागत आहे!")
    st.write("रुग्ण डेटाचा अभ्यास करा. CSV फाइल अपलोड करा.")

    st.file_uploader("📂 CSV डेटा अपलोड करा", type=["csv"])
    st.selectbox("🔍 फिल्टर", ["वय", "रुग्ण स्थिती", "ठिकाण"])

    st.image("sample_chart.png", caption="चाचणी स्टेटस विहंगावलोकन")

elif page == "Analysis":
    st.subheader("डेटा विश्लेषण (लवकरच)")
    st.info("इथे ग्राफ आणि अहवाल दिसतील.")

elif page == "Help":
    st.subheader("मदत")
    st.markdown("📧 संपर्क: support@statmate.ai")

st.markdown("---")
st.caption("© 2025 Statmate · Powered by Streamlit")
