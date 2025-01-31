from django.urls import path
from . import views

urlpatterns = [
    path("view_tests/", views.view_tests, name="view_tests"),
]
