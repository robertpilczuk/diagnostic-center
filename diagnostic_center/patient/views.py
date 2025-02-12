from django.shortcuts import render, redirect, get_object_or_404
from laboratory.models import LabTest, Appointment, TestResult
from .forms import AppointmentForm
from doctor.models import Prescription
from accounts.forms import PatientRegistrationForm


def patient_home(request):
    return render(request, "patient/patient_home.html")


def patient_register(request):
    if request.method == "POST":
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = PatientRegistrationForm()
    return render(request, "patient/patient_register.html", {"form": form})


def view_tests(request):
    tests = LabTest.objects.all()
    return render(request, "patient/view_tests.html", {"tests": tests})


def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        appointment = form.save(commit=False)
        appointment.patient = request.user
        appointment.save()
        return redirect("view_appointments")
    else:
        form = AppointmentForm()
    return render(request, "patient/book_appointment.html", {"form": form})


def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(
        Appointment, id=appointment_id, patient=request.user
    )
    appointment.status = "canceled"
    appointment.save()
    return redirect("view_appointments")


def view_prescription(request):
    prescription = Prescription.objects.filter(patient=request.user)
    return render(
        request, "patient/view_prescription.html", {"prescription": prescription}
    )


def confirm_reschedule_date(request, appointment_id):
    appointment = get_object_or_404(
        Appointment, id=appointment_id, patient=request.user
    )
    if request.method == "POST":
        new_date = request.POST.get("new_date")
        appointment.date = new_date
        appointment.status = "pending"
        appointment.save()
        return redirect("view_appointments")
    return render(
        request, "patient/confirm_reschedule_date.html", {"appointment": appointment}
    )


def view_test_result(request):
    tests = LabTest.objects.filter(patient=request.user)
    return render(request, "patient/view_test_result.html", {"tests": tests})


def view_test_results(request):
    test_results = TestResult.objects.filter(patient=request.user)
    return render(
        request, "patient/view_test_results.html", {"test_results": test_results}
    )


# Create your views here.
