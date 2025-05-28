import google.generativeai as genai
from django.conf import settings
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print(GEMINI_API_KEY)
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-pro')

def generate_text(prompt):
    try:
        GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        print(GEMINI_API_KEY)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
