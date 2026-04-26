import streamlit as st
from dotenv import load_dotenv
from google import genai
import os
import time

load_dotenv()

st.header("Make Your Text Professional")
st.divider()

apiKey = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=apiKey)

def stream_text(text):
    for word in text.split(" "):
        yield word + ' '
        time.sleep(0.05)
        

text = st.text_input("Write a text: ")

if text:
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = f"refurbish this text with professional tone and language: {text}"
    )
    
    st.write_stream(stream_text(response.text))
    

