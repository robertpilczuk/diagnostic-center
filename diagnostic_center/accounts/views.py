from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, UserLoginForm, PatientRegistrationForm
from accounts.models import User


def register(request):
    if request.method == "POST":
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = PatientRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


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
        request, "accounts/verify_laboratories.html", {"laboratory": laboratory}
    )


def view_doctors(request):
    doctors = User.objects.filter(is_doctor=True)
    return render(request, "accounts/view_doctors.html", {"doctors": doctors})


def verify_doctor(request, doctor_id):
    doctor = get_object_or_404(User, id=doctor_id, is_doctor=True)
    if doctor.method == "POST":
        doctor.is_verified = True
        doctor.save()
        return redirect("view_doctors")
    return render(request, "accounts/verify_doctor.html", {"doctor": doctor})


# Create your views here.
