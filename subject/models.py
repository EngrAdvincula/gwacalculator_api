from django.db import models

# Create your models here.
class SubList(models.Model):
    subject = models.CharField(max_length=100)
    units = models.IntegerField()