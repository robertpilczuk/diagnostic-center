from django.urls import path
from . import views

urlpatterns = [
    path("register/patient/", views.patient_register, name="patient_register"),
    path("patient_register", views.patient_register, name="patient_register"),
    path("view_tests/", views.view_tests, name="view_tests"),
    path("book_appointment/", views.book_appointment, name="book_appointment"),
    path(
        "cancel_appointment/<int:appointment_id>/",
        views.cancel_appointment,
        name="cancel_appointment",
    ),
    path("view_prescription/", views.view_prescription, name="view_prescription"),
    path(
        "confirm_reschedule_date/<int:appointment_id>/",
        views.confirm_reschedule_date,
        name="confirm_reschedule_date",
    ),
    path("view_test_result/", views.view_test_result, name="view_test_result"),
]
