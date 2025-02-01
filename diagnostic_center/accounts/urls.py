from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("view_laboratories/", views.view_laboratories, name="view_laboratories"),
    path(
        "verify_laboratories/<int:laboratory_id>/",
        views.verify_laboratories,
        name="verify_laboratories",
    ),
    path("view_doctors/", views.view_doctors, name="view_doctors"),
    path("verify_doctor/<int:doctor_id>/", views.verify_doctor, name="verify_doctor"),
]
