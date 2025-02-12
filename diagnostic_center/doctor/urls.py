from django.urls import path
from . import views

urlpatterns = [
    path("", views.doctor_home, name="doctor_home"),
    path("search_patient/", views.search_patient, name="search_patient"),
    path("write_prescription/", views.write_prescription, name="write_prescription"),
    path("view_test_results/", views.view_test_results, name="view_test_results"),
    path("view_prescriptions/", views.view_prescriptions, name="view_prescriptions"),
    path("order_lab_test/", views.order_lab_test, name="order_lab_test"),
    path("create_test_order/", views.create_test_order, name="create_test_order"),
]
