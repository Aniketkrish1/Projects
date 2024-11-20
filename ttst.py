import streamlit as st
import cohere

# Function to generate a story using Cohere API
def generate_story(prompt: str):
    api_key = "ts9WtKV5SkVD4K3izWV8idxNeaoBykiT7zJkTQbY"  # Replace with your actual Cohere API key
    co = cohere.Client(api_key)

    # Call the Cohere API to generate a story
    response = co.generate(
        prompt=prompt,
        max_tokens=300,  # You can adjust the length of the story here
        temperature=0.7,  # Adjust the creativity of the output
        stop_sequences=["\n"]  # Optional: stop generating if a newline is encountered
    )

    # Access the generated text from the response
    story = response.generations[0].text.strip()  # Correct way to access the text
    return story

# Streamlit interface
st.title("Text-to-Story Generator")
st.write("Enter a prompt, and the AI will generate a story for you!")

# Input text box for user to enter the prompt
input_text = st.text_area("Enter the text:", height=150)

# Button to generate the story
if st.button("Generate Story"):
    if input_text:
        story = generate_story(input_text)
        
        # Display the generated story
        st.write("**Generated Story:**")
        st.write(story)
    else:
        st.error("Please enter some text to generate a story.")
