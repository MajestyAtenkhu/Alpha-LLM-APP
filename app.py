
import streamlit as st
import openai
import os

# Get the API key from an environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI API client
openai.api_key = api_key

def generate_response(prompt):
    if prompt:
        try:
            # Use the OpenAI API to generate a response
            response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=100)

            # Return the response
            return response.choices[0].text.strip()
        except Exception as e:
            st.error(f"An error occurred: {e}")
            return None

def main():
    # Create a text input for the user's prompt
    prompt = st.text_input("Please enter your prompt:")

    # Create a button for the user to generate a response
    if st.button("Submit"):
        # If the prompt is not empty, generate a response
        if prompt:
            response = generate_response(prompt)

            # Display the response
            if response:
                st.text(response)

if __name__ == "__main__":
    main()

