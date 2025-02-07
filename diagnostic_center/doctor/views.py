from django.shortcuts import render, redirect
from .forms import PrescriptionForm, OrderLabTestForm
from .models import Prescription
from laboratory.models import LabTest


def doctor_home(request):
    return render(request, "doctor/home.html")


def search_patient(request):
    if request.method == "POST":
        query = request.POST.get("query")
        patients = User.objects.filter(is_patient=True, username__icontains=query)
        return render(request, "doctor/search_patient.html", {"patients": patients})
    return render(request, "doctor/search_patient.html")


def write_prescription(request):
    if request.method == "POST":
        form = PrescriptionForm(request.POST)
        prescription = form.save(commit=False)
        prescription.doctor = request.user
        prescription.save()
        return redirect("prescription_list")
    else:
        form = PrescriptionForm()
    return render(request, "doctor/write_prescription.html", {"form": form})


def view_test_results(request):
    tests = LabTest.objects.all()
    return render(request, "doctor/view_test_results.html", {"tests": tests})


def view_prescriptions(request):
    prescriptions = Prescription.objects.all()
    return render(
        request, "doctor/view_prescriptions.html", {"prescriptions": prescriptions}
    )


def order_lab_test(request):
    if request.method == "POST":
        form = OrderLabTestForm(request.POST)
        if form.is_valid():
            lab_test = form.save(commit=False)
            lab_test.ordered_by = request.user
            lab_test.save()
            return redirect("view_test_results")
    else:
        form = OrderLabTestForm()
    return render(request, "doctor/order_lab_test.html", {"form": form})


# Create your views here.
