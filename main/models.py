from django.db import models

# Create your models here.
class Toilet(models.Model):
    lon = models.FloatField()
    lat = models.FloatField()