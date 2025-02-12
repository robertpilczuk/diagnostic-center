from django.db import models
from accounts.models import User


class Patient(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="patient_profile"
    )
    pesel = models.CharField(max_length=11, unique=True)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.user.get_full_name()} (PESEL: {self.pesel})"
