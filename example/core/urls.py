from django.urls import path
from .views import Home # new


urlpatterns = [
    path("", Home.as_view(), name="home"), # new
]