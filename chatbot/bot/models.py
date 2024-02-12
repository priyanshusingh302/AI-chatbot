from django.db import models

class StringInput(models.Model):
    promt = models.CharField(max_length=255)
    context = models.CharField(max_length=255)

