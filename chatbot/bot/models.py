# models.py

from django.db import models

class StringInput(models.Model):
    promt = models.CharField(max_length=255)
