from django.db import models
from django.utils.html import format_html

from django.db import models

class Livraison(models.Model):
    # Informations générales
    transporteur = models.CharField(max_length=255)
    nombre_palettes = models.IntegerField()
    numero_commande = models.CharField(max_length=255)
    reserve = models.BooleanField(default=False)

    # Signatures
    nom_chauffeur = models.CharField(max_length=255)
    signature_chauffeur = models.ImageField(upload_to="signatures/")
    nom_employe = models.CharField(max_length=255)
    signature_employe = models.ImageField(upload_to="signatures/")

    # Horodatage
    date_heure = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Livraison {self.numero_commande} - Transporteur: {self.transporteur} - Employé: {self.nom_employe}"

    
    def signature_chauffeur_image(self):
        if self.signature_chauffeur:
            return format_html(
                '<img src="{}" width="200" height="100"/>',
                self.signature_chauffeur
            )
        return "Pas de signature"

    def signature_employe_image(self):
        if self.signature_employe:
            return format_html(
                '<img src="{}" width="200" height="100"/>',
                self.signature_employe
            )
        return "Pas de signature"

    signature_chauffeur_image.short_description = "Signature chauffeur"
    signature_employe_image.short_description = "Signature employé"

