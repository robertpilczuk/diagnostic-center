from django import forms
from .models import Prescription, TestOrder
from laboratory.models import LabTest


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ["patient", "description"]


class OrderLabTestForm(forms.ModelForm):
    class Meta:
        model = LabTest
        fields = ["name", "description"]


class TestOrderForm(forms.ModelForm):
    class Meta:
        model = TestOrder
        fields = ["patient", "test_name", "description"]
