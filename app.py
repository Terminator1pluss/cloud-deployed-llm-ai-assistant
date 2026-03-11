import streamlit as st

st.title("Cloud-Deployed AI Assistant")

question = st.text_input("Ask something")

if question:
    st.write("AI answer will appear here.")