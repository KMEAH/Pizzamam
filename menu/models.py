from django.db import models
from django.db.models.fields import BooleanField, CharField, FloatField

class Pizza(models.Model):
    nom = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=400)
    prix = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.nom
