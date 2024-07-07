from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    # slug = models.CharField(max_length=50)
    sortdescription = models.CharField(max_length=50)
    fulldescription = models.CharField(max_length=50)  
    group_tag = models.CharField(max_length=50)

class subCategory(models.Model):
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    # slug = models.CharField(max_length=50)
    sortdescription = models.CharField(max_length=50)
    fulldescription = models.CharField(max_length=50)  
    group_tag = models.CharField(max_length=50)

class Products(models.Model):
    productCat = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    # slug = models.CharField(max_length=50)
    sortdescription = models.CharField(max_length=50)
    fulldescription = models.CharField(max_length=50)  
    group_tag = models.CharField(max_length=50)
    packtype = models.CharField(max_length=50)
    size = models.IntegerField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    photoM = models.ImageField(upload_to="Files",blank=True,null=True)

class Inventry(models.Model):
    name = models.CharField(max_length=50)
    purchase = models.IntegerField()
    stock = models.IntegerField()
    photoM = models.ImageField(upload_to="Files/Main",blank=True,null=True)
    offer = models.IntegerField()
    date = models.DateField()
    status = models.CharField(max_length=50)
    