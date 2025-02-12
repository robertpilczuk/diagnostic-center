from django.db import models
from accounts.models import User


class LabTest(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    laboratory = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={"is_laboratory": True}
    )

    def __str__(self):
        return self.name


class AppointmentRequest(models.Model):
    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"is_patient": True},
        related_name="patient_appointment_requests",
    )
    laboratory = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={"is_laboratory": True},
        related_name="laboratory_appointments_request",
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

    def __str__(self):
        return f"Appointment for {self.laboratory} on {self.date}"


# TODO  czy to nie to samo co AppointmentRequest!!!
class Appointment(models.Model):
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
        related_name="laboratory_appointments_appointment",
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

    def __str__(self):
        return f"Appointment request for {self.patient} on {self.date}"


class Report(models.Model):
    appointment = models.OneToOneField(AppointmentRequest, on_delete=models.CASCADE)
    report_file = models.FileField(upload_to="reports/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for appointment {self.appointment}"


class TestResult(models.Model):
    patient = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={"is_patient": True}
    )
    test_name = models.CharField(max_length=100)
    result = models.TextField()
    result_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Test Result for {self.patient} - {self.test_name}"


# Create your models here.
