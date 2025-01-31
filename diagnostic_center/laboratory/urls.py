from django.urls import path
from . import views

urlpatterns = [
    path("add_lab_test/", views.add_lab_test, name="add_lab_test"),
    path(
        "view_appointment_requests/",
        views.view_appointment_request,
        name="view_appointment_request",
    ),
    path(
        "accept_appointment/<int:appointment_id>/",
        views.accept_appointment,
        name="accept_appointment",
    ),
    path(
        "reschedule_appointment/<int:appointment_id>/",
        views.reschedule_appointment,
        name="reschedule_appointment",
    ),
    path(
        "reject_appointment/<int:appointment_id>/",
        views.reject_appointment,
        name="reject_appointment",
    ),
]
