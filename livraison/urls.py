from django.urls import path
from .views import delivery_consignation_view, expedition_consignation_view, historique_view, annuler_livraison

urlpatterns = [
    path("", delivery_consignation_view, name="delivery_consignation"),
    path("delivery_consignation/", delivery_consignation_view, name="delivery_consignation"),
    path("expedition_consignation/", expedition_consignation_view, name="expedition_consignation"),
    path("historique/", historique_view, name="historique"),
    path('annuler-livraison/<int:livraison_id>/', annuler_livraison, name='annuler_livraison'),
]
