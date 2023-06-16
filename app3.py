
import streamlit as st
import openai
import os
os.environ["OPENAI_API_KEY"] = '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'  # replace 'your-api-key' with your actual OpenAI API key

def generate_response(prompt):
    if prompt:
        # Use the OpenAI API to generate a response
        response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=100)

        # Return the response
        return response.choices[0].text.strip()


def main():
    # Create a text input for the user's prompt
    prompt = st.text_input("Please enter your prompt:")

    # If the prompt is not empty, generate a response
    if prompt:
        response = generate_response(prompt)

        # Display the response
        st.text(response)



        if __name__ == "__main__":  main()

