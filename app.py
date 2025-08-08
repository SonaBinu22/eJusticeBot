import streamlit as st
from chatbot import get_response

# App UI
st.set_page_config(page_title="eJustice Legal Aid Chatbot", page_icon="⚖️")

st.title("⚖️ eJustice - Legal Aid Chatbot")
st.markdown("Welcome! I'm here to help you with basic legal information in India.")

# User input
user_input = st.text_input("Ask your legal question:")

if user_input:
    response = get_response(user_input)
    st.markdown(f"**Chatbot:** {response}")
