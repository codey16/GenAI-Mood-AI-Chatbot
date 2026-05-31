import streamlit as st
from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

# -----------------------
# Configuration
# -----------------------

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-2603",
    temperature=0.5
)

st.set_page_config(
    page_title="Mood AI Agent",
    page_icon="🤖",
    layout="wide"
)

# -----------------------
# Custom CSS
# -----------------------

st.markdown("""
<style>

.main{
    background-color:#0E1117;
}

.title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:white;
}

.subtitle{
    text-align:center;
    color:#A0A0A0;
    margin-bottom:20px;
}

.stChatMessage{
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------
# Sidebar
# -----------------------

with st.sidebar:

    st.title("🎭 AI Personality")

    mood = st.radio(
        "Choose AI Mood",
        [
            "😡 Angry",
            "😂 Funny",
            "😢 Sad"
        ]
    )

    st.divider()

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -----------------------
# Personality Selection
# -----------------------

if mood == "😡 Angry":
    system_prompt = """
    You are an Angry AI-Agent.
    Reply aggressively, impatiently,
    and slightly annoyed.
    """

elif mood == "😂 Funny":
    system_prompt = """
    You are a Funny AI-Agent.
    Reply with humor, jokes,
    and funny comments.
    """

else:
    system_prompt = """
    You are a Sad AI-Agent.
    Reply in a depressed,
    emotional and gloomy tone.
    """

# -----------------------
# Session State
# -----------------------

if "messages" not in st.session_state:

    st.session_state.messages = [
        SystemMessage(content=system_prompt)
    ]

# Update personality if changed

if isinstance(
    st.session_state.messages[0],
    SystemMessage
):
    st.session_state.messages[0] = SystemMessage(
        content=system_prompt
    )

# -----------------------
# Header
# -----------------------

st.markdown(
    '<p class="title">🤖 Mood AI Agent</p>',
    unsafe_allow_html=True
)

st.markdown(
    f'<p class="subtitle">Current Mood: {mood}</p>',
    unsafe_allow_html=True
)

# -----------------------
# Display Messages
# -----------------------

for msg in st.session_state.messages:

    if isinstance(msg, HumanMessage):

        with st.chat_message("user"):
            st.markdown(msg.content)

    elif isinstance(msg, AIMessage):

        with st.chat_message("assistant"):
            st.markdown(msg.content)

# -----------------------
# Chat Input
# -----------------------

prompt = st.chat_input(
    "Ask something..."
)

if prompt:

    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = model.invoke(
                st.session_state.messages
            )

            st.markdown(response.content)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )