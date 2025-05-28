"""
URL configuration for taskmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import HelloView
from crawler.views import crawl

handler500 = "taskmanager.views.custom_500_handler"

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', include('tasks.urls')),
    path('profile/<str:username>/', views.user_profile),
    path('hello/', views.say_hello_with_method),

    # URL and parameters
    path('users/', include('users.urls')),

    # Class-based views
    path('hello-cbv/', HelloView.as_view()),

    # Path Parameter
    path('paths/<int:id>/', views.user_detail),

    # Validation
    # Path Parameter
    path('hello/<str:name>/', views.say_hello_validation),
    # Query Parameter
    path('query-validation/', views.search),
    # Header Parameter
    path('header-validation/', views.check_client),

    # Custom error handler
    path('raise-error-500/', views.raise_error_500),
    
    path('raise-error-500/', views.say_hello_in_background),

    # Dependancies
    path('random-quote/', views.random_quote),
    path('crawl-page/', crawl, name='crawl'),
    path('crawl/', crawl, name='crawl'),

    path('api/tasks-drf/', views.TaskView.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)