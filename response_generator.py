#response_generator.py

from langchain.chains.question_answering import load_qa_chain

def generate_response(openai, index, prompt):
    if prompt:
        try:
            # Query the index for the most relevant documents
            relevant_documents = index.query(prompt)

            # Load a question answering chain
            chain = load_qa_chain(openai, chain_type="qa")

            # Run the chain with the relevant documents and the prompt
            response = chain.run(input_documents=relevant_documents, question=prompt)

            # Return the response
            return response
        except Exception as e:
            return f"An error occurred: {e}"
