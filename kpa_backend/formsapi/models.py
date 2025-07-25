from django.db import models
from django.contrib.postgres.fields import JSONField  # For Django 3.1+, else use models.JSONField

class WheelSpecification(models.Model):
    form_number = models.CharField(max_length=100, db_index=True)
    submitted_by = models.CharField(max_length=100)
    submitted_date = models.DateField()
    fields = models.JSONField()  # Use JSONField for flexible fields storage
    created_at = models.DateTimeField(auto_now_add=True)

class BogieChecksheet(models.Model):
    form_number = models.CharField(max_length=100, db_index=True)
    inspection_by = models.CharField(max_length=100)
    inspection_date = models.DateField()
    bogie_details = models.JSONField()
    bogie_checksheet = models.JSONField()
    bmbc_checksheet = models.JSONField()
    status = models.CharField(max_length=32, default="Saved")
    created_at = models.DateTimeField(auto_now_add=True)
