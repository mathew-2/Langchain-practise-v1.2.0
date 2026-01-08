import requests
import streamlit as st


def get_ollama_response(input_text):

    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json={"input": {"topic": input_text}})

    return response.json()["output"]

st.title("Local LLM with LangChain and Streamlit")
input_text = st.text_input("Enter the essay topic here:")

if input_text:
    output = get_ollama_response(input_text)
    st.write(output)