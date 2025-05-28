from django.http import HttpResponse

def users_list(request):
    return HttpResponse("List of Users")

def user_detail(request, id):
    return HttpResponse(f"Details of User {id}")
