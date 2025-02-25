# Generated by Django 3.2.25 on 2025-02-07 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(limit_choices_to={'is_doctor': True}, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_prescriptions', to='accounts.user')),
                ('patient', models.ForeignKey(limit_choices_to={'is_patient': True}, on_delete=django.db.models.deletion.CASCADE, related_name='patient_prescriptions', to='accounts.user')),
            ],
        ),
    ]
