from django import forms
from .models import LabTest, AppointmentRequest, Report


class LabTestForm(forms.ModelForm):
    class Meta:
        model = LabTest
        fields = ["name", "description"]


class AppointmentRequestForm(forms.ModelForm):
    class Meta:
        model = AppointmentRequest
        fields = ["patient", "date"]


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["report_file"]
