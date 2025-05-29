import google.generativeai as genai
from django.conf import settings
import os
import numpy as np
import chromadb
from django.http import JsonResponse
from .chroma import add_to_chroma, query_chroma

client = chromadb.Client()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-2.0-flash')

def generate_text(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
    
def generate_rag_text(prompt):
    # context_chunks = retrieve_relevant_chunks(prompt)
    context_chunks = query_chroma([prompt])
    print("DEBUG")
    context = [doc for sublist in context_chunks['documents'] for doc in sublist]

    print(context)

    full_prompt = f"""Gunakan konteks ini untuk menjawab pertanyaan.
Konteks:
{context}

Pertanyaan:
{prompt}
"""

    response = model.generate_content(full_prompt)
    return response.text.strip()

def add_document(request):
    add_to_chroma(
        documents=["Pembuat modul ini adalah Pradana Google Developer Expert"],
        ids=["doc1"]
    )
    return JsonResponse({"status": "added"})

def search_document(request):
    results = query_chroma(["AI-generated"])
    return JsonResponse(results)
