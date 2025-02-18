from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from doctor.models import SPECIALIZATION_CHOICES


class UserRegistrationForm(UserCreationForm):
    USER_TYPE_CHOICES = [
        ("is_empty", "Choose type"),
        ("is_patient", "Patient"),
        ("is_doctor", "Doctor"),
        ("is_laboratory", "Laboratory"),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)
    specialization = forms.ChoiceField(choices=SPECIALIZATION_CHOICES, required=False)

    pesel = forms.CharField(max_length=11, required=True)
    date_of_birth = forms.DateField(required=True)
    address = forms.CharField(max_length=255, required=False)
    phone_number = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = [
            "user_type",
            "username",
            "password1",
            "password2",
            "specialization",
            "is_admin",
            "is_laboratory",
            "is_doctor",
            "is_patient",
            # "is_empty",
            "pesel",
            "date_of_birth",
            "address",
            "phone_number",
        ]


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class PatientRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "email",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        if commit:
            user.save()
        return user
