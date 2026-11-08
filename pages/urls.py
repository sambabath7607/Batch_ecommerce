
from django.urls import path

from .views import Accueil, a_propos, service, contact , ajouter_panier ,afficher_panier
from .views import suprimer_product,modifier_quantite, suprimer_panier


urlpatterns  = [
    path("" , Accueil.as_view() , name="accueil"),
    path("a_propos/" , a_propos , name="a_propos"),
    path("service/" , service , name="service"),
    path("contact/" , contact , name="contact"),
    path("ajouter_panier/<int:pk>/" , ajouter_panier , name="ajouter_panier"),
    path("afficher_panier/" , afficher_panier , name="afficher_panier"),
    path("suprimer_product/<int:pk>/" , suprimer_product , name="suprimer_product"),
    path("modifier_quantite/<int:pk>/" , modifier_quantite , name="modifier_quantite"),
    path("suprimer_panier/" , suprimer_panier , name="suprimer_panier"),
]