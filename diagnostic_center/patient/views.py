from django.shortcuts import render, redirect, get_object_or_404
from laboratory.models import LabTest, Appointment
from .forms import AppointmentForm
from doctor.models import Prescription


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


# Create your views here.
