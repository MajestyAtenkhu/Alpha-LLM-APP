#document_index.py
import request 
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

def load_documents_and_create_index(document_url)

    # Download the document
    response = requests.get(document_url)
    document_content = response.text
    # Load the documents
    loader = TextLoader(document_content)

    # Create the index
    index = VectorstoreIndexCreator().from_loaders([loader])

    return index
