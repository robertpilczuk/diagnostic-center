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
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"is_patient": True},
        related_name="patient_appointments",
    )
    laboratory = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"is_laboratory": True},
        related_name="laboratory_appointments",
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


class Report(models.Model):
    appointment = models.OneToOneField(AppointmentRequest, on_delete=models.CASCADE)
    report_file = models.FileField(upload_to="reports/")
    uploaded_at = models.DateTimeField(auto_now_add=True)


# TODO  czy to nie to samo co AppointmentRequest!!!
class Appointment(models.Model):
    patient = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={"is_patient": True}
    )
    laboratory = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={"is_laboratory": True}
    )
    date = models.DateTimeField()
    prescription = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("accepted", "Accepted"),
            ("rejected", "Rejected"),
        ],
    )


# Create your models here.
