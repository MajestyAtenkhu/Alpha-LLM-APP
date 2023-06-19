#document_index.py
import pdfplumber
import requests
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import QAGenerationChain

def load_documents_and_create_index(document_url):
    # Modify the URL to point to the raw PDF file
    raw_url = document_url.replace("github.com", "raw.githubusercontent.com").replace("/blob", "")

    # Download the document
    response = requests.get(raw_url)
    with open('document.pdf', 'wb') as f:
        f.write(response.content)

    # Extract text from the PDF
    with pdfplumber.open('document.pdf') as pdf:
        text = '\n'.join(page.extract_text() for page in pdf.pages)

    # Load the documents
    loader = TextLoader(text)

    # Create the index
    index = VectorstoreIndexCreator().from_loaders([loader])

    return index



