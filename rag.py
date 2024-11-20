import PyPDF2
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Step 1: Extract Text from a PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

# Step 2: Split Text into Chunks
def split_text_into_chunks(text, max_length=500):
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0
    for word in words:
        current_chunk.append(word)
        current_length += len(word) + 1  # Including space
        if current_length >= max_length:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_length = 0
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

# Step 3: Create Embeddings and Build FAISS Index
def build_faiss_index(chunks):
    retriever = SentenceTransformer("all-MiniLM-L6-v2")
    chunk_embeddings = retriever.encode(chunks, convert_to_tensor=False)
    dimension = chunk_embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(chunk_embeddings))
    return index, retriever

# Step 4: Retrieve Relevant Chunks
def retrieve_relevant_chunks(query, retriever, index, chunks, top_k=5):
    query_embedding = retriever.encode([query], convert_to_tensor=False)
    distances, indices = index.search(np.array(query_embedding), top_k)
    return [chunks[i] for i in indices[0]]

# Step 5: Summarize Using a Transformer Model
def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=200, min_length=50, truncation=True)
    return summary[0]['summary_text']

# Step 6: RAG Pipeline for PDF Summarization
def rag_pdf_summary(pdf_path, query):
    # Extract and preprocess PDF text
    text = extract_text_from_pdf(pdf_path)
    chunks = split_text_into_chunks(text)
    
    # Build FAISS index
    index, retriever = build_faiss_index(chunks)
    
    # Retrieve relevant chunks
    relevant_chunks = retrieve_relevant_chunks(query, retriever, index, chunks)
    combined_text = " ".join(relevant_chunks)
    
    # Summarize retrieved text
    summary = summarize_text(combined_text)
    return summary

# Test the RAG System
pdf_path = "C:/Users/ANIKET/OneDrive/Documents/nav.pdf"  # Replace with your PDF path
query = "Summarize the main points of this document"
summary = rag_pdf_summary(pdf_path, query)
print("Summary:", summary)
