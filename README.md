# Gemini RAG Chatbot

A beginner-friendly Retrieval-Augmented Generation (RAG) chatbot built with **LangChain**, **Google Gemini**, and **Chroma**.

This project demonstrates the full basic RAG pipeline:

- loading text and PDF documents
- splitting content into chunks
- creating embeddings
- storing vectors in Chroma
- retrieving relevant context
- generating answers with Gemini

## Features

- Text file loading with LangChain loaders
- PDF file loading with LangChain PDF loader
- Text chunking with `RecursiveCharacterTextSplitter`
- Gemini embeddings for semantic search
- Chroma vector store for retrieval
- Gemini chat model for final answer generation
- Structured responses with confidence and source tracking
- Simple scripts for learning and portfolio use

## Tech Stack

- **Python**
- **LangChain**
- **Google Gemini API**
- **Chroma**
- **python-dotenv**
- **Pydantic**

## Models Used

- **Chat model:** `gemini-2.5-flash-lite`
- **Embedding model:** `gemini-embedding-001`

These models were chosen because they are suitable for low-cost learning, testing, and small-scale RAG experimentation.

## How the RAG Pipeline Works

1. A document is loaded from text or PDF.
2. The content is split into smaller chunks.
3. Each chunk is converted into embeddings.
4. The embeddings are stored in Chroma.
5. A question is compared against the stored vectors.
6. The most relevant chunks are retrieved.
7. Gemini generates the final answer using the retrieved context.

## Project Structure

```text
gemini-rag-chatbot/
├── src/
│   ├── pdf_loader.py
│   ├── rag_pipeline.py
|   ├── text_loader.py
│   └── web_loader.py
├── data/
│   ├── sample.pdf
│   └── sample.txt
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```
## Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/gemini-rag-chatbot.git
cd gemini-rag-chatbot
```

### 2. Create a virtual environment
On Windows PowerShell:

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API key
Create a **.env file** in the project root:

```bash
GOOGLE_API_KEY=your_google_api_key_here
```

### Running the Project
Run the main RAG pipeline:

```bash
python src/rag_pipeline.py
```

Run the text loader:

```bash
python src/text_loader.py
```

Run the PDF loader:

```bash
python src/pdf_loader.py
```

### Sample Files
The repository includes a small sample PDF and text file for testing document loading and retrieval.

```bash
data/sample.txt
data/sample.pdf
```
If you replace them with your own files, keep the content simple and readable so the loader output remains clear.

### What I Learned
This project helped me understand:

how RAG pipelines are built end to end
how document loaders work
how chunking affects retrieval quality
how embeddings convert text into vectors
how a vector database supports semantic search
how retrieval and generation are connected
how to manage environments with venv
how to use .env files for API keys
how to swap model providers without rewriting the whole pipeline

### Notes
This project is intended for learning, experimentation, and portfolio use.
API keys are never committed to the repository.
The project uses a local virtual environment and a .env file for secrets management.
Chroma can be configured to persist locally if needed for future improvements.

### Future Improvements
Add support for more document types
Add a web UI
Add citation highlighting in answers
Add conversation memory
Add evaluation metrics for retrieval quality
Add document ingestion from folders and websites
Add streaming responses
Add a better prompt tuning workflow

### License
This project is licensed under the MIT License. See the LICENSE file for details.
