import sys
sys.path.append(r'C:\Users\maten\Documents\Resume\Majesty Resume V 5.1.pdf')  # replace 'path_to_directory' with the actual path to the directory

import streamlit as st
import openai
import os
from document_index import load_documents_and_create_index
from response_generator import generate_response

# Get the API key from an environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI API client
openai.api_key = api_key

# Load your documents and create an index
document_path = 'r'C:\Users\maten\Documents\Resume\Majesty Resume V 5.1.pdf'  # replace with the actual path to your document
index = load_documents_and_create_index(document_path)

def main():
    # Create a text input for the user's prompt
    prompt = st.text_input("Please enter your prompt:")

    # Create a button for the user to generate a response
    if st.button("Submit"):
        # If the prompt is not empty, generate a response
        if prompt:
            response = generate_response(openai, index, prompt)

            # Display the response
            if response:
                st.text(response)

if __name__ == "__main__":
    main()
