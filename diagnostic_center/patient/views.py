from django.shortcuts import render, redirect
from laboratory.models import LabTest
from .forms import AppointmentForm


def view_tests(request):
    tests = LabTest.objects.all()
    return render(request, "patient/view_tests.html", {"tests": tests})


def book_appointment(request):
    if request.method == "POST":
        appointment = form.save(commit=False)
        appointment.patient = request.user
        appointment.save()
        return redirect("view_appointments")
    else:
        form = AppointmentForm()
    return render(request, "patient/book_appointment.html", {"form": form})


# Create your views here.
