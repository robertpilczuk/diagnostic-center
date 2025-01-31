from django.urls import path
from . import views

urlpatterns = [
    path("view_tests/", views.view_tests, name="view_tests"),
    path("book_appointment/", views.book_appointment, name="book_appointment"),
    path(
        "cancel_appointment/<int:appointment_id>/",
        views.cancel_appointment,
        name="cancel_appointment",
    ),
    path("view_prescription/", views.view_prescription, name="view_prescription"),
]
