import streamlit as st
from coordinator import decide_agent
from memory import add_memory

st.set_page_config(page_title="Multi-Agent AI Chatbot")

st.title("Multi-Agent AI Chatbot")

# Ask for Groq API key
groq_key = st.sidebar.text_input(
    "Enter your Groq API Key",
    type="password"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

prompt = st.chat_input("Ask something")

if prompt:

    if not groq_key:
        st.warning("Please enter your Groq API Key in the sidebar.")
        st.stop()

    add_memory(st.session_state.messages, "user", prompt)

    st.chat_message("user").write(prompt)

    response = decide_agent(
        st.session_state.messages,
        prompt,
        groq_key
    )

    add_memory(st.session_state.messages, "assistant", response)

    st.chat_message("assistant").write(response)