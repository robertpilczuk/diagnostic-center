from django.urls import path
from . import views

urlpatterns = [
    path("search_patient/", views.search_patient, name="search_patient"),
    path("write_prescription/", views.write_prescription, name="write_prescription"),
    path("view_test_results/", views.view_test_results, name="view_test_results"),
]
