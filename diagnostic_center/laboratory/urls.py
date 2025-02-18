from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.laboratory_home, name="laboratory_home"),
    path("add_lab_test/", views.add_lab_test, name="add_lab_test"),
    path("view_lab_tests/", views.view_lab_tests, name="view_lab_tests"),
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
    path(
        "upload_report/<int:appointment_id>/", views.upload_report, name="upload_report"
    ),
    path("view_reports/", views.view_reports, name="view_reports"),
    path("register_sample/", views.register_sample, name="register_sample"),
    path(
        "enter_test_result/<int:test_request_id>/",
        views.enter_test_result,
        name="enter_test_result",
    ),
    path(
        "download_test_result/<int:test_result_id>/",
        views.download_test_result,
        name="download_test_result",
    ),
]
