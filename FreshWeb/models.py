# Create your models here.
from django.db import models

class NewCart(models.Model):
    productId = models.IntegerField()
    productValue= models.CharField(max_length=256)
    productName=  models.CharField(max_length=256)
    productQuantity = models.IntegerField()
    username = models.CharField(max_length=256)
    productImg = models.ImageField(upload_to="Files",blank=True,null=True)

class Wishlist(models.Model):
    wishId = models.IntegerField()
    wishValue= models.CharField(max_length=256)
    wishName=  models.CharField(max_length=256)
    # wishQuantity = models.IntegerField(blank=True,null=True)    
    username = models.CharField(max_length=256)
    wishImg = models.ImageField(upload_to="Files",blank=True,null=True)

class Checkouts(models.Model):
    productName = models.CharField(max_length=255)
    productValue = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    username = models.EmailField()
    # total = models.IntegerField()
    
    
