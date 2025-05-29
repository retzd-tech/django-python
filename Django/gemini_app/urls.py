from django.urls import path
from .views import home, add_data_view
from .chroma import add_to_chroma

urlpatterns = [
    path("", home, name="home"),
    # path("add-data", add_to_chroma, name="home"),
     path("add-data/", add_data_view, name="add_data"), # Use a trailing slash for consistency
]
