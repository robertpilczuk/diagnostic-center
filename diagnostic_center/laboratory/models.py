from django.db import models
from accounts.models import User


class LabTest(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    laboratory = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={"is_laboratory": True}
    )


class AppointmentRequest(models.Model):
    patient = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={"is_patient": True}
    )
    laboratory = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={"is_laboratory": True}
    )
    date = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("accepted", "Accepted"),
            ("rejected", "Rejected"),
        ],
    )


# Create your models here.
