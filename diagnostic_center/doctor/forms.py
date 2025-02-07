from django import forms
from .models import Prescription
from laboratory.models import LabTest


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ["patient", "description"]


class OrderLabTestForm(forms.ModelForm):
    class Meta:
        model = LabTest
        fields = ["name", "description"]
