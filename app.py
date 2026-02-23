import streamlit as st
from core.config import get_api_key
from services.gemini_service import GeminiService
from memory.session_memory import initialize_memory, add_message, get_history

st.set_page_config(page_title="AI Career Advisor", layout="wide")

st.title("AI Career Advisor Chatbot")

api_key = get_api_key()

if not api_key:
    st.error("API Key not configured.")
    st.stop()

initialize_memory()

if "service" not in st.session_state:
    st.session_state.service = GeminiService(api_key)

# Display History
for msg in get_history():
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask your career question...")

if user_input:
    add_message("user", user_input)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing..."):
            response = st.session_state.service.generate_response(
                user_input,
                get_history()
            )
            st.markdown(response)

    add_message("assistant", response)