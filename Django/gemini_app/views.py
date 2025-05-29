from django.shortcuts import render, redirect
from .utils import generate_text, generate_rag_text

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt # Important for testing with POSTman/curl
import json
from .chroma import add_to_chroma # Import your chroma service function

def home(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        if prompt:
            messages = request.session.get("messages", [])
            messages.append({"role": "user", "content": prompt})

            # output = generate_text(prompt)
            output = generate_rag_text(prompt)
            messages.append({"role": "bot", "content": output})

            request.session["messages"] = messages
            return redirect("home")

    messages = request.session.get("messages", [])
    return render(request, "chat.html", {"messages": messages})


@csrf_exempt # For simplicity during development/testing. In production, use proper CSRF protection.
def add_data_view(request):
    if request.method == 'POST':
        try:
            # Get the JSON payload from the request body
            data = json.loads(request.body)

            # Extract the necessary data from the JSON payload
            documents = data.get('documents')
            ids = data.get('ids')
            metadatas = data.get('metadatas')
            embeddings = data.get('embeddings') # Optional

            # Basic validation
            if not documents or not ids:
                return JsonResponse({"error": "Missing 'documents' or 'ids' in the payload"}, status=400)

            # Call your add_to_chroma function
            add_to_chroma(
                documents=documents,
                ids=ids,
                metadatas=metadatas,
                embeddings=embeddings
            )

            return JsonResponse({"message": "Data successfully added to ChromaDB!"}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON payload"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Only POST requests are allowed for this endpoint."}, status=405)
