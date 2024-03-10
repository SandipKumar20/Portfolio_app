import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Sandip Kumar")
    content = """
    I am a python programmer, and a machine learning engineer. I love coding, reading.
    I have worked on python projects, deep learning projects.
    """
    st.info(content)