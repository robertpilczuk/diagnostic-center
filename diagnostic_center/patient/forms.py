from django import forms
from laboratory.models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["laboratory", "date", "prescription"]
