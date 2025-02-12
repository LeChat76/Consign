from django.contrib import admin
from django.utils.html import format_html
from .models import Livraison

class LivraisonAdmin(admin.ModelAdmin):
    list_display = (
        "date_heure",
        "transporteur",
        "numero_commande",
        "nombre_palettes",
        "reserve",
        "nom_chauffeur",
        "signature_chauffeur_preview",
        "nom_employe",
        "signature_employe_preview",
    )

    def signature_chauffeur_preview(self, obj):
        if obj.signature_chauffeur:
            return format_html('<img src="{}" width="100" height="50" />', obj.signature_chauffeur.url)
        return "Pas de signature"

    signature_chauffeur_preview.short_description = "Signature Chauffeur"

    def signature_employe_preview(self, obj):
        if obj.signature_employe:
            return format_html('<img src="{}" width="100" height="50" />', obj.signature_employe.url)
        return "Pas de signature"

    signature_employe_preview.short_description = "Signature Employé"

# Enregistrer le modèle avec la classe personnalisée
admin.site.register(Livraison, LivraisonAdmin)
