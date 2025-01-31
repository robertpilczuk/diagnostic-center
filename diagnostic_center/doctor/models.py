from django.db import models
from accounts.models import User


class Prescription(models.Model):
    doctor = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={"is_doctor": True}
    )
    patient = models.ForeignKey(
        User, on_delete=models.CASCADE, limit_choices_to={"is_patient": True}
    )
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


# Create your models here.
