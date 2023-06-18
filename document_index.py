#document_index.py

from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

def load_documents_and_create_index(document_path)
    # Load the documents
    loader = TextLoader(document_path)

    # Create the index
    index = VectorstoreIndexCreator().from_loaders([loader])

    return index
