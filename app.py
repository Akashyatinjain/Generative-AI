import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

# Personas matching chatbot.py
PERSONAS = {
    "1. Funny AI": "You are a FUNNY Kinf of person,Please respond in a Funny manner",
    "2. Professional AI": "You are a Professional AI",
    "3. Romantic AI": "You are a Romantic AI"
}

# Model initialization matching chatbot.py
@st.cache_resource
def get_model():
    return ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        temperature=0.9
    )

model = get_model()

def extract_text(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list) and len(content) > 0:
        first = content[0]
        if isinstance(first, dict) and "text" in first:
            return first["text"]
        elif hasattr(first, "text"):
            return first.text
        return str(first)
    return str(content)

# AI Persona Selection matching chatbot.py
st.sidebar.header("AI Model Type")
selected_persona = st.sidebar.selectbox(
    "Choose Your AI model type:",
    options=list(PERSONAS.keys()),
    index=0
)

# Reset messages if persona changes or on initial load
if "current_persona" not in st.session_state or st.session_state.current_persona != selected_persona:
    st.session_state.current_persona = selected_persona
    st.session_state.messages = [
        SystemMessage(content=PERSONAS[selected_persona])
    ]

# Display Title and Current Active Persona
st.title("🤖 AI Chatbot")
st.caption(f"Currently chatting with: **{selected_persona}**")

# Display conversation history (excluding SystemMessage)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(extract_text(msg.content))
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(extract_text(msg.content))

# Chat input
if prompt := st.chat_input("Type your message... (type 0 to reset)"):
    if prompt.strip() == "0":
        st.session_state.messages = [
            SystemMessage(content=PERSONAS[selected_persona])
        ]
        st.rerun()
    else:
        # Append and display user message
        st.session_state.messages.append(HumanMessage(content=prompt))
        with st.chat_message("user"):
            st.markdown(prompt)

        # Invoke model
        with st.chat_message("assistant"):
            with st.spinner("Generating response..."):
                response = model.invoke(st.session_state.messages)
                bot_text = extract_text(response.content)
                st.session_state.messages.append(AIMessage(content=response.content))
                st.markdown(bot_text)
