from langchain_community.document_loaders import (WebBaseLoader)
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

def web_loader():
    loader = WebBaseLoader(
        "https://en.wikipedia.org/wiki/Web_scraping", bs_kwargs={"parse_only": None}
    )
    documents = loader.load()

    print(f"Loaded {len(documents)} document(s) from web")
    print(f"Source: {documents[0].metadata.get('source', 'N/A')}")
    print(f"Content length: {len(documents[0].page_content)} characters")
    print(f"Preview: {documents[0].page_content[:200]}...")

if __name__ == "__main__":
     web_loader()

