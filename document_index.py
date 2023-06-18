from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
import pdfplumber
import requests

def load_documents_and_create_index(document_url):
    # Download the document
    response = requests.get(document_url)
    with open('document.pdf', 'wb') as f:
        f.write(response.content)

    # Extract text from the PDF
    with pdfplumber.open('document.pdf') as pdf:
        text = '\n'.join(page.extract_text() for page in pdf.pages)

    # Load the documents
    loader = TextLoader(text)  # corrected line

    # Create the index
    index = VectorstoreIndexCreator().from_loaders([loader])

    return index


