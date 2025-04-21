import streamlit as st

st.title("My First APP")

name = st.text_area("What's your name?")

if name:
  st.write(f"Hello, {name}!")
