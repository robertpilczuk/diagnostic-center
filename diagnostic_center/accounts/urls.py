from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("view_laboratories/", views.view_laboratories, name="view_laboratories"),
    path(
        "verify_laboratory/<int:laboratory_id>/",
        views.verify_laboratory,
        name="verify_laboratory",
    ),
]
