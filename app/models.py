from django.db import models
from django.utils import timezone
import random

# Create your models here.
class Parcel(models.Model):
    tracking_number = models.CharField(max_length=20, unique=True)  # Numéro de suivi par défaut
    adress_dep = models.CharField(max_length=100)
    adress_arr = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.IntegerField(default=0)  # 0: En attente, 1: En cours, 2: Livré
    date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.tracking_number:
            self.tracking_number = 'FR'+ str(random.randint(1000000000, 9999999999))  # Génère
            super().save(*args, **kwargs)  # Appelle la méthode save() de la classe parente pour enregistrer l'objet
    def __str__(self):
        return f"Colis n°{self.id} - {self.weight}"