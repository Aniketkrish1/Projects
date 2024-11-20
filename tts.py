import streamlit as st
import pyttsx3

# Text-to-Speech class
class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()  # Initialize the pyttsx3 engine
    
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

# Streamlit interface
st.title("Text-to-Speech Converter")
st.write("Enter the text below and the system will speak the text out loud!")

# Input text box for user to enter the message
input_message = st.text_area("Enter the text:", height=150)

# Button to trigger text-to-speech
if st.button("Convert to Speech"):
    if input_message:
        # Create an instance of TextToSpeech and speak the text
        tts = TextToSpeech()
        tts.speak(input_message)
        st.success("Speech has been generated!")
    else:
        st.error("Please enter some text to convert to speech.")
