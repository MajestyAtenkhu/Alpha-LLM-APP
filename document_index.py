#document_index.py

from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
import PyPDF2
import requests
from io import BytesIO

def load_documents_and_create_index(document_url):

    # Download the document
    response = requests.get(document_url)
    
    # Create a BytesIO object from the response content
    file = BytesIO(response.content)

    # Create a PDF file reader object
    pdf_reader = PyPDF2.PdfFileReader(file)

    # Initialize an empty string to hold the text
    text = ""

    # Loop through each page in the PDF and extract the text
    for page_num in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_num)
        text += page.extractText()

    
    # Load the documents
    loader = TextLoader(document_content)

    # Create the index
    index = VectorstoreIndexCreator().from_loaders([loader])

    return index
