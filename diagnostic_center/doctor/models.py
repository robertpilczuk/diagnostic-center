from django.db import models
from accounts.models import User


class Prescription(models.Model):
    doctor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"is_doctor": True},
        related_name="doctor_prescriptions",
    )
    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"is_patient": True},
        related_name="patient_prescriptions",
    )
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


# Create your models here.
