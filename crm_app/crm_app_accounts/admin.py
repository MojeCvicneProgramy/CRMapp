from django.contrib import admin

# Register your models here.

# from .models import Customer  # Customer je zadefinovaný class v models.py
# namiesto toho lepšie použiť imortovanie všetkého:
from .models import *

admin.site.register(Customer)  # zaregistrovanie zakaznika
admin.site.register(Product)  # zaregistrovanie produktu
admin.site.register(Order)  # zaregistrovanie objednávky aby ich zobrazovalo na stránke