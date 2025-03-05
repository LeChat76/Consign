from django.shortcuts import render
from django.http import JsonResponse
from .models import Livraison
import base64
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt

def delivery_consignation_view(request):
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
            type_operation='delivery',
        )
        return JsonResponse({"message": "Livraison enregistrée avec succès"}, status=201)

    return render(request, "delivery_consignation.html")

def expedition_consignation_view(request):
    if request.method == "POST":
        # Récupérer les données
        transporteur = request.POST.get("transporteur")
        nombre_palettes = request.POST.get("nombre_palettes")
        numero_commande = request.POST.get("numero_commande")
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
            nom_chauffeur=nom_chauffeur,
            signature_chauffeur=signature_chauffeur_file,
            nom_employe=nom_employe,
            signature_employe=signature_employe_file,
            type_operation='expedition',
        )
        return JsonResponse({"message": "Livraison enregistrée avec succès"}, status=201)

    return render(request, "expedition_consignation.html")

@csrf_exempt
def annuler_livraison(request, livraison_id):
    if request.method == 'POST':
        try:
            livraison = Livraison.objects.get(id=livraison_id)
            print(f"Avant : recordDisabled = {livraison.recordDisabled}")
            
            livraison.recordDisabled = True
            livraison.save()

            print(f"Après : recordDisabled = {livraison.recordDisabled}")
            return JsonResponse({'success': True})
        except Livraison.DoesNotExist:
            print("Enregistrement non trouvé.")
            return JsonResponse({'error': 'Enregistrement introuvable.'}, status=404)
    print("Méthode non autorisée.")
    return JsonResponse({'error': 'Méthode non autorisée.'}, status=405)


def historique_view(request):
    # Récupérer toutes les livraisons
    livraisons = Livraison.objects.filter(recordDisabled=False).order_by("-date_heure")
    return render(request, 'historique.html', {'livraisons': livraisons})
