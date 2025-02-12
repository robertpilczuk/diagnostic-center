from django.db import models
from accounts.models import User
from patient.models import Patient


class TestOrder(models.Model):
    doctor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="test_orders"
    )
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="test_orders"
    )
    test_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Test Order for {self.patient} by {self.doctor}"


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
