import streamlit as st
from main import generate_response

st.set_page_config(
    page_title="AI Email Responder",
    page_icon="📧",
    layout="centered"
)

st.title("📧 AI Email Responder")

email = st.text_area(
    "Paste Customer Email",
    height=200,
    placeholder="Enter customer email here..."
)

if st.button("Generate Response"):

    if email.strip():

        with st.spinner("Analyzing Email..."):

            intent, reply = generate_response(email)

        st.subheader("Detected Intent")
        st.success(intent)

        st.subheader("Generated Reply")
        st.write(reply)

    else:
        st.warning("Please enter an email.")