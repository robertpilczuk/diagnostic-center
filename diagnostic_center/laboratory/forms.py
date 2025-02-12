from django import forms
from .models import (
    LabTest,
    AppointmentRequest,
    Report,
    Appointment,
    Sample,
    TestResult,
    TestRequest,
    TestOrder,
)


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


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["laboratory", "date", "prescription"]


# class SampleRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Sample
#         fields = ["patient", "test_name", "sample_date"]


# class TestResultForm(forms.ModelForm):
#     class Meta:
#         model = TestResult
#         fields = ["patient", "test_name", "result"]


class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ["sample_id", "patient"]


class TestRequestForm(forms.ModelForm):
    class Meta:
        model = TestRequest
        fields = ["sample", "test_order"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["sample"].queryset = Sample.objects.all()
        self.fields["test_order"].queryset = TestOrder.objects.filter(is_completed=True)


class TestResultForm(forms.ModelForm):
    class Meta:
        model = TestResult
        fields = ["result"]
