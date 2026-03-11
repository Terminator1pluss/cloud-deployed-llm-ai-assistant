import streamlit as st

st.title("Cloud-Deployed AI Assistant")
st.write("Ask a question and the AI will respond.")

question = st.text_input("Enter your question")

if question:
    st.write("You asked:", question)
    st.info("AI response will appear here soon.")