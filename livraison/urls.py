from django.urls import path
from .views import consignation_view, historique_view

urlpatterns = [
    path("", consignation_view, name="consignation"),
    path("consignation/", consignation_view, name="consignation"),
    path("historique/", historique_view, name="historique"),
]
