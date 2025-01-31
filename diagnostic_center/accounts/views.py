from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, UserLoginForm
from accounts.models import User


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = UserLoginForm()
    return render(request, "accounts/login.html", {"form": form})


def view_laboratories(request):
    laboratories = User.object.filter(is_laboratory=True)
    return render(
        request, "accounts/view_laboratories.html", {"laboratories": laboratories}
    )


def verify_laboratories(request, laboratory_id):
    laboratory = get_object_or_404(User, id=laboratory_id, is_laboratory=True)
    if request.method == "POST":
        laboratory.is_verified = True
        laboratory.save()
        return redirect("view_laboratories")
    return render(
        request, "accounts/verify_laboratory.html", {"laboratory": laboratory}
    )


# Create your views here.
