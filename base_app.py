import streamlit as st

st.title("My First APP")

name = st.text_area("What's your name?") # or use st.text_input for a smaller text input box (one line)

if name:
  st.write(f"Hello, {name}!")
