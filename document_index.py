#document_index.py

from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

def load_documents_and_create_index(r'C:\Users\maten\Documents\Resume\Majesty Resume V 5.1.pdf')
    # Load the documents
    loader = TextLoader(r'C:\Users\maten\Documents\Resume\Majesty Resume V 5.1.pdf')

    # Create the index
    index = VectorstoreIndexCreator().from_loaders([loader])

    return index
