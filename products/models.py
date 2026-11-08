from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Products(models.Model):
    user = models.ForeignKey(User,null=True , blank=True , on_delete=models.CASCADE)
    name = models.CharField(max_length=130)
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='products', )
    date = models.DateTimeField(auto_now_add=True)
    category  = models.CharField(max_length=100)
    stock= models.IntegerField(default=0)
    #slug = models.SlugField()


    def __str__(self):
        return f"{self.name}"
    #user
    #d-create
class Panier(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        created = models.DateTimeField(auto_now_add=True)
        def __str__(self):
            return f"{self.user.username}"
class Panier_items(models.Model):
        panier = models.ForeignKey(Panier , on_delete=models.CASCADE)
        product = models.ForeignKey(Products , on_delete=models.CASCADE)
        quantite = models.PositiveIntegerField(default=1)
        ordered = models.BooleanField(default=False)
        def __str__(self):
            return f"{self.product.name} {self.quantite}"
class Commande(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    statut= models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2 , default=0 )
    def __str__(self):
        return f"{self.user.username}"
class Commande_items(models.Model):
    commande = models.ForeignKey(Commande , on_delete=models.CASCADE , related_name="items")
    product = models.ForeignKey(Products , on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2 , default=0)
    def __str__(self):
        return f"{self.commande.user.username} --------------{self.quantite}"








