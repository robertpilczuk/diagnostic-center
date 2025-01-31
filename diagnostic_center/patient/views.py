from django.shortcuts import render
from laboratory.models import LabTest


def view_tests(request):
    tests = LabTest.objects.all()
    return render(request, "patient/view_tests.html", {"tests": tests})


# Create your views here.
