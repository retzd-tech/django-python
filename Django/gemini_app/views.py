from django.shortcuts import render, redirect
from .utils import generate_text

def home(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        if prompt:
            output = generate_text(prompt)
            request.session['output'] = output
            return redirect('home')  # redirect to avoid resubmitting on reload
    output = request.session.pop('output', '')
    return render(request, "index.html", {"output": output})