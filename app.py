import streamlit as st
import requests

st.set_page_config(page_title="Cloud AI Assistant")

st.title("Cloud-Deployed AI Assistant")
st.write("Ask any question and the AI assistant will respond.")

question = st.text_input("Enter your question")

def get_response(q):
    url = "https://api-inference.huggingface.co/models/google/flan-t5-small"
    payload = {"inputs": q}

    try:
        response = requests.post(url, json=payload, timeout=20)
        data = response.json()
        return data[0]["generated_text"]
    except:
        return "The AI model is currently loading. Please try again."

if question:
    answer = get_response(question)
    st.success(answer)