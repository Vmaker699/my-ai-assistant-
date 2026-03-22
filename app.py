import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage

# Setup local LLM (install Ollama first: ollama.com, then `ollama pull llama3.2`)
llm = ChatOllama(model="llama3.2", temperature=0.7)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🧠 My AI Assistant")

for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        st.chat_message("user").write(message.content)
    else:
        st.chat_message("assistant").write(message.content)

if prompt := st.chat_input("Ask me anything!"):
    st.session_state.messages.append(HumanMessage(content=prompt))
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        response = llm.invoke(st.session_state.messages)
        st.write(response.content)
        st.session_state.messages.append(AIMessage(content=response.content))
