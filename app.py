import streamlit as st
import subprocess

# Page Configuration
st.set_page_config(page_title="Multifunctional Interface", layout="wide")

# Title and Description
st.title("Multifunctional Interface")


# Input and Button Handling
task = st.radio("Choose a task:", ["Text-to-Speech", "Text-to-Video", "Text-to-Story", "RAG PDF"])

if st.button("Run"):
    if task == "Text-to-Speech":
            st.write("Running Text-to-Speech...")
            subprocess.run(["streamlit","run", "tts.py"])
    elif task == "Text-to-Video":
        st.write("Generating video from text...")
        subprocess.run(["streamlit","run", "ttv.py"])
    elif task == "Text-to-Story":
        st.write("Generating story from text...")
        subprocess.run(["streamlit","run", "ttst.py"])
    elif task == "RAG PDF":
        st.write("Performing RAG on PDF...")
        subprocess.run(["streamlit","run", "rag.py"])
