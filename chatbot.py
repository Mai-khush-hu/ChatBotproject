import streamlit as st

st.title("Hola Amigo AI")

st.chat_input("Enter Something")

with st.sidebar:
    st.write("This is sidebar")
    st.button("Sidebar button")
    st.button("New Chats")
    