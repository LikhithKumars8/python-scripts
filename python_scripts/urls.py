from django.urls import path
from .views import JokesData

urlpatterns = [
    path("jokes/", JokesData.as_view())
]