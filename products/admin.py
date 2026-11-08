from django.contrib import admin

from products.models import Products , Panier , Panier_items

from products.models import Commande , Commande_items


# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category' , 'content' , 'date')
    search_fields = ('name', 'category')
    list_filter = ('category','date')
admin.site.register(Products ,ProductsAdmin )

class PanierAdmin(admin.ModelAdmin):
    list_display = ['user' , 'created']
admin.site.register(Panier , PanierAdmin )
class Panier_itemsAdmin(admin.ModelAdmin):
    list_display = ['panier' , 'product' , 'quantite']
admin.site.register(Panier_items , Panier_itemsAdmin )


class CommandeAdmin(admin.ModelAdmin):
    list_display = ['user' , 'created_at' , "statut", 'total']
admin.site.register(Commande , CommandeAdmin )

class commande_itemsAdmin(admin.ModelAdmin):
    list_display = ['commande' , 'product' , 'quantite']
admin.site.register(Commande_items , commande_itemsAdmin )



