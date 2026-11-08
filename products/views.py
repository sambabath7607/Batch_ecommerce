from http.client import responses
from itertools import product

from django.http import HttpResponse
from django.shortcuts import render ,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from pyexpat.errors import messages

from .models import Products ,Panier,Panier_items

from .models import Commande , Commande_items
class ProductsDetailView(DetailView):
    template_name = "products/detail.html"
    model = Products
    pk_url_kwarg = 'pk'
    context_object_name = 'obj'
from .forms import ProductsCreateForm


# Create your views here.
# CRUD ------------------------------------------
# fbv
# CRUD ------------------------------------------
# cbv
class ProductsListeView(ListView):
    template_name = "products/listeproducts.html"
    model = Products
    context_object_name = 'obj'
    paginate_by = 4
    def get_queryset(self):
        return Products.objects.filter(user = self.request.user)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['manage_products'] = True
        return context

class ProductsCreateView(CreateView):
    template_name = "products/createproducts.html"
    model = Products
    fields = ['name' , 'content' , 'price', 'img', 'category' , 'stock']
    success_url = reverse_lazy('liste_cbv')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProductsUpdateView(UpdateView):
    template_name = "products/updateproducts.html"
    model = Products
    form_class = ProductsCreateForm
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('liste_cbv')

class ProductsDeleteView(DeleteView):
    template_name = "products/deleteproducts.html"
    model = Products
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('liste')

#---------------------------------------------------
#GESTIONS DE PANIER
#ajouter un ele au panier
def ajouter_panier(request, pk):
    product  = Products.objects.get(pk=pk)
    panier , create = Panier.objects.get_or_create(user = request.user)
    panier_items , created_items = Panier_items.objects.get_or_create(
        panier = panier,
        product=product,
        defaults = {'quantite' : 1})
    if created_items :
        panier_items.quantite = 1
    else :
        panier_items.quantite +=1
    panier_items.save()
    return redirect('afficher_panier_db')


#afficher le apnier
def afficher_panier(request ):

    panier , create = Panier.objects.get_or_create(user=request.user)
    panier_items = Panier_items.objects.filter(panier=panier)
    return render(request, 'afficher_panier_db.html' ,{
        "panier" : panier,
        "panier_items" : panier_items  ,
        'message' : 'commander'} )

def surcharge_ajouter_panier(request ):
    message = ""
    if request.method == 'POST' :
        if 'commande' in request.POST:
            message ='commander'
    return render(request, 'afficher_panier_db.html' ,{
        'message' : message  })

def modifier_quantite_product(request , pk ):
    quantite = Panier_items.objects.get(pk=pk)
    if request.method == "POST":
        if "plus" in  request.POST :
            quantite.quantite +=1
        if "moins" in request.POST  :
            quantite.quantite -= 1
            if quantite.quantite <1:
                quantite.quantite = 1

    quantite.save()
    return redirect('afficher_panier_db')
def supremer_product(request,pk):
    Panier_items.objects.get(pk=pk).delete()
    return redirect('afficher_panier_db')
def sup_panier(request):
    panier, _ = Panier.objects.get_or_create(user=request.user)
    panier_items = Panier_items.objects.filter(panier=panier)
    panier_items.delete()
    return redirect('afficher_panier_db')




#------------------------------------------------------
#GESTION DE COMMANDE

def commande(request):
    user = request.user
    panier, _ = Panier.objects.get_or_create(user=user)
    panier_items = panier.panier_items_set.all()
    if  panier_items.exists() :
        commande = Commande.objects.create(
                user=user,
                statut="entente",
            )
    else :

        return redirect("afficher_panier_db")



    total = 0
    for ele in panier_items:
            total += ele.product.price * ele.quantite
            Commande_items.objects.create(
                commande=commande,
                product=ele.product,
                quantite=ele.quantite,
                price=ele.product.price,
            )
    commande.total = total
    commande.save()
    panier_items.delete()

    return render(request, 'commande.html', {
            "commande": commande,
            "commande_items": commande.items.all(),
        })


def  ancien_commande(request):
    user = request.user
    commande = Commande.objects.filter(user=user)
    commande_items = Commande_items.objects.all()
    return render(request , 'ancien_commande.html' , {"commande" : commande,
                                                      "commande_items" : commande_items})
#---------------------------------------------------------------------------------------

#Intégration des systèmes de paiement dans notre projet STRIPE









