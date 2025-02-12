from django.shortcuts import render
from django.http import JsonResponse
from .models import Livraison
import base64
from django.core.files.base import ContentFile

def consignation_view(request):
    if request.method == "POST":
        # Récupérer les données
        transporteur = request.POST.get("transporteur")
        nombre_palettes = request.POST.get("nombre_palettes")
        numero_commande = request.POST.get("numero_commande")
        reserve = request.POST.get("reserve") == "oui"
        nom_chauffeur = request.POST.get("nom_chauffeur")
        signature_chauffeur_data = request.POST.get("signature_chauffeur")  # Base64
        nom_employe = request.POST.get("nom_employe")
        signature_employe_data = request.POST.get("signature_employe")  # Base64

        # Vérifie si toutes les données nécessaires sont présentes
        if not all([transporteur, nombre_palettes, numero_commande, nom_chauffeur, signature_chauffeur_data, nom_employe, signature_employe_data]):
            return JsonResponse({"message": "Toutes les données ne sont pas présentes !"}, status=400)

        # Décoder les images en fichiers
        signature_chauffeur_file = ContentFile(base64.b64decode(signature_chauffeur_data.split(",")[1]), "signature_chauffeur.png")
        signature_employe_file = ContentFile(base64.b64decode(signature_employe_data.split(",")[1]), "signature_employe.png")

        # Enregistrer les données dans la base de données
        Livraison.objects.create(
            transporteur=transporteur,
            nombre_palettes=int(nombre_palettes),
            numero_commande=numero_commande,
            reserve=reserve,
            nom_chauffeur=nom_chauffeur,
            signature_chauffeur=signature_chauffeur_file,
            nom_employe=nom_employe,
            signature_employe=signature_employe_file,
        )
        return JsonResponse({"message": "Livraison enregistrée avec succès"}, status=201)

    return render(request, "consignation.html")


def historique_view(request):
    # Récupérer toutes les livraisons
    livraisons = Livraison.objects.all().order_by("-date_heure")
    return render(request, "historique.html", {"livraisons": livraisons})
