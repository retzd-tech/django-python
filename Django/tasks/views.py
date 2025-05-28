import json
from django.http import JsonResponse
from .models import Task
from django.views.decorators.csrf import csrf_exempt

# 📌 Feature: GET (Query Params), POST (Body), CRUD
# @csrf_exempt
# def task_list_create(request):
#     if request.method == 'GET':
#         is_completed = request.GET.get('completed')  # Feature: Query Parameters
#         tasks = Task.objects.all()
#         if is_completed is not None:
#             tasks = tasks.filter(is_completed=(is_completed.lower() == 'true'))
#         data = list(tasks.values())
#         return JsonResponse(data, safe=False)

#     if request.method == 'POST':
#         body = json.loads(request.body)
#         task = Task.objects.create(
#             title=body.get('title'),
#             description=body.get('description', ''),
#             is_completed=body.get('is_completed', False)
#         )
#         return JsonResponse({'id': task.id, 'message': 'Task created'}, status=201)

# # 📌 Feature: Path Parameters, PUT/DELETE Methods, CRUD
# @csrf_exempt
# def task_detail_update_delete(request, task_id):
#     try:
#         task = Task.objects.get(pk=task_id)
#     except Task.DoesNotExist:
#         return JsonResponse({'error': 'Task not found'}, status=404)

#     if request.method == 'GET':
#         return JsonResponse({
#             'id': task.id,
#             'title': task.title,
#             'description': task.description,
#             'is_completed': task.is_completed,
#         })

#     if request.method == 'PUT':
#         body = json.loads(request.body)
#         task.title = body.get('title', task.title)
#         task.description = body.get('description', task.description)
#         task.is_completed = body.get('is_completed', task.is_completed)
#         task.save()
#         return JsonResponse({'message': 'Task updated'})

#     if request.method == 'DELETE':
#         task.delete()
#         return JsonResponse({'message': 'Task deleted'})

# 📌 Feature: Cookie & Header Parameters
def debug_headers_cookies(request):
    cookie = request.COOKIES.get('sessionid')
    user_agent = request.headers.get('User-Agent')
    return JsonResponse({
        'user_agent': user_agent,
        'session_cookie': cookie,
    })

# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

@csrf_exempt
@api_view(['GET', 'POST'])
def task_list_create(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def task_detail_update_delete(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=404)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        task.delete()
        return Response(status=204)

@api_view(['GET'])
def debug_headers_cookies(request):
    return Response({
        'headers': dict(request.headers),
        'cookies': request.COOKIES
    })
