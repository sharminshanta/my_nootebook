from django.utils import timezone
from django.db import models

class Contact(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  phone = models.IntegerField()
  timestamp = models.DateTimeField(default=timezone.now)
