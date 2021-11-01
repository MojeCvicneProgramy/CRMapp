from django.db import models

# Create your models here.

class Customer (models.Model):
    name = models.CharField(max_length=200, null=True)  # null=True sa dáva aby nevypísalo ERROR keď je nevyplnená hodnota
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
# tento Customer sa zaregistruje v admin.py aby ho zobrazilo na admin stránke

# aby sa zobrazovalo v zozname meno zákezníka namiesto "Customer object(1)" zadefinujeme funkciu:
    def __str__(self):
        return self.name

class Product (models.Model):
    # zadefinujeme premennú STATUS aby sme ho mohli zvoliť z dropdown menu (tuples)
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
        )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)  # výber choices ťahá z premennej CATEGORY zadefinovanej vyššie
    destcription = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Order (models.Model):
    # zadefinujeme premennú STATUS aby sme ho mohli zvoliť z dropdown menu (tuples)
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
        )
    # customer = ...zadefinujeme neskôr
    # product = ...zadefinujeme neskôr
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)  # výber choices ťahá z premennej STATUS zadefinovanej vyššie