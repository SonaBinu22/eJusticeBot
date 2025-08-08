import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="eJustice Bot", layout="centered")
st.title("⚖️ eJustice – Legal Aid Chatbot for Citizens")
st.markdown("Get legal guidance based on Indian laws in simple steps.")

st.markdown("---")

# Chat interaction
user_input = st.text_input("🗨️ Ask your question:")
if user_input:
    response = get_response(user_input)
    st.markdown("### 🤖 Chatbot Reply")
    st.success(response)

st.markdown("---")
st.info("This bot is for informational purposes only and not a substitute for professional legal advice.")
