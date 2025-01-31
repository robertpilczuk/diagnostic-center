from django import path
from . import views

urlpatterns = [
    path("add_lab_test/", views.add_lab_test, name="add_lab_test"),
    path(
        "view_appointment_requests/",
        views.view_appointment_request,
        name="view_appointment_request",
    ),
]
