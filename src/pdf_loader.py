from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

def pdf_loader():
    pdf_path = Path(__file__).resolve().parent / "sample.pdf"

    if not pdf_path.is_file():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    loader = PyPDFLoader(str(pdf_path))
    documents = loader.load()

    print(f"Loaded {len(documents)} document(s) from PDF")
    for i, doc in enumerate(documents):
        print(f"Document {i + 1} Content Preview: {doc.page_content[:100]}...")
        print(f"Metadata: {doc.metadata}")

if __name__ == "__main__":
    pdf_loader()
