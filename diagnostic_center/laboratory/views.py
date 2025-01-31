from django.shortcuts import render, redirect
from .forms import LabTestForm, AppointmentRequestForm
from .models import LabTest, AppointmentRequest


def add_lab_test(request):
    if request.method == "POST":
        form = LabTestForm(request.POST)
        if form.is_valid():
            lab_test = form.save(commit=False)
            lab_test.laboratory = request.user
            lab_test.save()
            return redirect("lab_test_list")
    else:
        form = LabTestForm()
    return render(request, "laboratory/add_lab_test.html", {"form": form})


def view_appointment_request(request):
    request = AppointmentRequest.objects.filter(laboratory=request.user)
    return render(
        request, "laboratory/view_appointment_request.html", {"request": request}
    )


# Create your views here.
