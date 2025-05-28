from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http import JsonResponse
import logging
from faker import Faker

logger = logging.getLogger(__name__)

def user_profile(request, username):
    return HttpResponse(f"Profile page for {username}")

def say_hello(request):
    print(request.method)
    return HttpResponse("Hello there! Say Hello Function!")

@csrf_exempt
def say_hello_with_method(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Hello!', 'method': 'GET'})
    
    if request.method == 'POST':
        return JsonResponse({'message': 'Hello!', 'method': 'POST'})
    

class HelloView(View):
    def get(self, request):
        return HttpResponse("GET request: Hello!")

    def post(self, request):
        return HttpResponse("POST request: Data submitted.")

def user_detail(request, id):
    return HttpResponse(f"Details of User {id}")

# views.py
def say_hello_validation(request, name):
    if not name.isalpha():
        return HttpResponseBadRequest("Name must contain only letters")
    return HttpResponse(f"Hello, {name}!")

def search(request):
    q = request.GET.get('q')
    page = request.GET.get('page', '1')

    if not q:
        return HttpResponseBadRequest("Missing search query")

    if not page.isdigit():
        return HttpResponseBadRequest("Page must be a number")

    return HttpResponse(f"Searching for '{q}' on page {page}")

def check_client(request):
    client_version = request.headers.get('X-Client-Version')

    if not client_version:
        return HttpResponseBadRequest("Missing X-Client-Version header", status=420)

    if not client_version.startswith("v"):
        return HttpResponseBadRequest("Invalid version format")

    return HttpResponse(f"Client version accepted: {client_version}")


def custom_500_handler(request):
    logger.error("Unhandled server error", exc_info=True)
    return JsonResponse({"error": "Something went wrong"}, status=500)

def raise_error_500():
    1 / 0  # triggers 500


def say_hello_in_background(request):
    say_hello.delay("Altman")  # 👈 runs later, not now
    return JsonResponse({"status": "ok"})

fake = Faker()

def random_quote(request):
    return JsonResponse({
        "quote": fake.sentence(),
        "author": fake.name()
    })

from rest_framework.views import APIView
from rest_framework.response import Response

class TaskView(APIView):
    def get(self, request):
        return Response({"message": "GET - list tasks"})

    def post(self, request):
        data = request.data  # Incoming JSON/body data
        return Response({"message": "POST - create task", "data": data})