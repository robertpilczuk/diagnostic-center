from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReportForm, LabTestForm
from .models import (
    LabTest,
    Appointment,
    AppointmentRequest,
    Report,
)


def laboratory_home(request):
    return render(request, "laboratory/home.html")


def add_lab_test(request):
    if request.method == "POST":
        form = LabTestForm(request.POST)
        if form.is_valid():
            lab_test = form.save(commit=False)
            lab_test.laboratory = request.user
            lab_test.save()
            return redirect("view_lab_tests")
    else:
        form = LabTestForm()
    return render(request, "laboratory/add_lab_test.html", {"form": form})


def view_lab_tests(request):
    tests = LabTest.objects.all()
    return render(request, "laboratory/view_lab_tests.html", {"tests": tests})


def view_appointment_request(request):
    appointments = Appointment.objects.filter(status="pending")
    return render(
        request,
        "laboratory/view_appointment_request.html",
        {"appointments": appointments},
    )


def accept_appointment(request, appointment_id):
    appointment = get_object_or_404(AppointmentRequest, id=appointment_id)
    appointment.status = "accepted"
    appointment.save()
    return redirect("view_appointment_requests")


def reschedule_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == "POST":
        new_date = request.POST.get("new_date")
        appointment.date = new_date
        appointment.status = "pending"
        appointment.save()
        return redirect("view_appointment_request")
    return render(
        request, "laboratory/reschedule_appointment.html", {"appointment": appointment}
    )


def reject_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.status = "rejected"
    appointment.save()
    return redirect("view_appointment_requests")


def upload_report(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.appointment = appointment
            report.save()
            return redirect("view_reports")
    else:
        form = ReportForm()
    return render(
        request,
        "laboratory/upload_report.html",
        {"form": form, "appointment": appointment},
    )


def view_reports(request):
    reports = Report.objects.all()
    return render(request, "laboratory/view_reports.html", {"reports": reports})


# Create your views here.
