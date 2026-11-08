from IPython.core.display import JSON
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView

from products.models import Products


# Create your views here.
class Accueil(ListView):
    template_name = 'accueil.html'
    model = Products
    context_object_name = 'obj'
    paginate_by = 4

def a_propos(request):
    D  ={}
    all_objects = Products.objects.all()
    i = 0
    for ele in all_objects :
        D["name" +str(i)] = ele.name
        D["content" +str(i)] = ele.content
        D["price" +str(i)] = ele.price
        i+=1


    return JsonResponse(D)
def service(request):
    liste = ['red' , 'yellow'  , 'gray' , 'aqua' , 'pink']
    return render(request, 'service.html' ,{"liste" :liste , })

def contact(request):

    return render(request, 'contact.html')

#-------------------------------------------------------------------------------------------
def ajouter_panier(request, pk):
    product = Products.objects.get(pk=pk)
    #product = get_object_or_404(Products,pk=pk)

    panier = request.session.get("panier" , {})
    pk = str(pk)
    if pk not in  panier :
        panier[pk] = {
            'name'  : product.name,
            'price' :float( product.price),
            'quantite' :1

        }
    else :
        panier[pk]["quantite"] +=1
    request.session["panier"] = panier
    return redirect("afficher_panier")


def afficher_panier(request) :
    panier = request.session["panier"]
    return render(request , "afficher_panier.html" , {'panier' : panier} )

def suprimer_product(request , pk):
    panier = request.session["panier"]
    pk = str(pk)
    if pk in panier:
        del panier[pk]
    request.session["panier"] = panier
    return redirect("afficher_panier")

def modifier_quantite(request , pk):
    panier = request.session['panier']
    pk =str(pk)
    if request.method =="POST":
        if 'plus' in request.POST:
            panier[pk]['quantite'] +=1
        if 'moins' in request.POST:
            panier[pk]['quantite'] -= 1
            if  panier[pk]['quantite']<1:
              panier[pk]['quantite'] = 1
        request.session["panier"] = panier
    return redirect("afficher_panier")


def suprimer_panier(request):

    if 'panier' in request.session:
         request.session['panier']= {}
    return redirect("afficher_panier")






