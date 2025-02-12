from django.db import models
from accounts.models import User
from patient.models import Patient


SPECIALIZATION_CHOICES = [
    ("Pediatrics", "Pediatrics"),
    ("Surgery", "Surgery"),
    ("Psychiatry", "Psychiatry"),
    ("Cardiology", "Cardiology"),
    ("Dermatology", "Dermatology"),
    ("Orthopedics", "Orthopedics"),
    ("Neurology", "Neurology"),
    ("Radiology", "Radiology"),
    ("Anesthesiology", "Anesthesiology"),
    ("Oncology", "Oncology"),
    ("Gynecology", "Gynecology"),
    ("Urology", "Urology"),
    ("Endocrinology", "Endocrinology"),
    ("Gastroenterology", "Gastroenterology"),
    ("Pulmonology", "Pulmonology"),
    ("Nephrology", "Nephrology"),
    ("Ophthalmology", "Ophthalmology"),
    ("Otolaryngology", "Otolaryngology"),
    ("Emergency Medicine", "Emergency Medicine"),
    ("Family Medicine", "Family Medicine"),
]


class Doctor(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="doctor_profile"
    )
    license_number = models.CharField(max_length=50, unique=True)
    specialization = models.CharField(max_length=100, choices=SPECIALIZATION_CHOICES)

    def __str__(self):
        return f"{self.user.get_full_name()} (License: {self.license_number})"


class Specialization(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


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
