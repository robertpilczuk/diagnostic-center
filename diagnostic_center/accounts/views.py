from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, UserLoginForm, PatientRegistrationForm
from accounts.models import User


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if not form.is_valid():
            print(form.errors)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_patient:
                    return redirect("patient_home")
                return redirect("home")
            else:
                form.add_error(None, "Invalid username or password.")
        else:
            form.add_error(None, "Invalid form submission.")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.is_patient:
                return redirect("patient_home")
            return redirect("login")
        else:
            print("Form errors:", form.errors)
    else:
        form = UserRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})


def patient_register(request):
    if request.method == "POST":
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts/login")
    else:
        form = PatientRegistrationForm()
    return render(request, "accounts/patient_register.html", {"form": form})


# def user_login(request):
#     if request.method == "POST":
#         form = UserLoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data["username"],
#                 password=form.cleaned_data["password"],
#             )
#             if user is not None:
#                 login(request, user)
#                 return redirect("home")
#     else:
#         form = UserLoginForm()
#     return render(request, "accounts/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("accounts/login")


def view_laboratories(request):
    laboratories = User.objects.filter(is_laboratory=True)
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
    if request.method == "POST":
        doctor.is_verified = True
        doctor.save()
        return redirect("view_doctors")
    return render(request, "accounts/verify_doctor.html", {"doctor": doctor})


# Create your views here.
