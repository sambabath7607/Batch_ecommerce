from django.urls import path

from .views import ProductsListeView , ProductsCreateView , ProductsUpdateView,ProductsDeleteView,ProductsDetailView
from .views import ajouter_panier ,afficher_panier ,modifier_quantite_product, supremer_product ,sup_panier

from .views import commande , surcharge_ajouter_panier , ancien_commande
urlpatterns = [


    path("", ProductsListeView.as_view(), name='liste_cbv'),
    path("create_cbv/", ProductsCreateView.as_view(), name='create_cbv'),
    path("update_cbv/<int:pk>/", ProductsUpdateView.as_view(), name='update_cbv'),
    path("delete_cbv/<int:pk>/", ProductsDeleteView.as_view(), name='delete_cbv'),
    path("detail_cbv/<int:pk>/", ProductsDetailView.as_view(), name='detail_cbv'),
    #----------------------------------------------
    #GESTIOM DE PANIER
    path("ajouter_panier_db/<int:pk>/" , ajouter_panier ,name='ajouter_panier_db'),
    path("afficher_panier_db/" , afficher_panier ,name='afficher_panier_db'),
    path("modifier_quantite_db/<int:pk>/" , modifier_quantite_product ,name='modifier_quantite_db'),
    path("supremer_product_db/<int:pk>/" , supremer_product ,name='supremer_product_db'),
    path("suprimer_panier/" , sup_panier ,name='suprimer_panier'),
    path("commande/" , commande ,name='commande'),
    path("ancien_commande/" , ancien_commande ,name='ancien_commande'),
    path("surcharge_ajouter_panier/" , surcharge_ajouter_panier ,name='surcharge_ajouter_panier'),

]