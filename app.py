
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

with st.sidebar.expander("🔐 Login"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.success(f"Welcome, {username}!")

if page == "Home":
    st.subheader("Welcome to Statmate!")
    st.write("Analyze patient cohorts, clinical trials, and healthcare insights.")

    st.file_uploader("📂 Upload Clinical Dataset (.csv)", type=["csv"])
    st.selectbox("🔍 Filter by", ["Age", "Condition", "Trial Site"])

    st.image("sample_chart.png", caption="Trial Status Overview")

elif page == "Analysis":
    st.subheader("Data Analysis (Coming Soon)")
    st.info("This section will show live graphs and cohort reports.")

elif page == "Help":
    st.subheader("Help & Support")
    st.markdown("For assistance, contact us at [support@statmate.ai](mailto:support@statmate.ai)")

st.markdown("---")
st.caption("© 2025 Statmate · Powered by Streamlit")
