from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list_create), # GET all or POST create
    path('<int:task_id>/', views.task_detail_update_delete), # GET, PUT, DELETE by ID
    path('debug/', views.debug_headers_cookies),
]

