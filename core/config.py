import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def get_api_key():

    
    api_key = os.getenv("gemini_key")
    if api_key:
        return api_key

   
    try:
        return st.secrets["GOOGLE_API_KEY"]
    except Exception:
        return None
