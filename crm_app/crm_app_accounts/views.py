from django.shortcuts import render
from django.http import HttpResponse
from .models import *  # naimportovanie celej databázy vytvorenej v models.py

def home(request):  # dashboard
    orders = Order.objects.all()  # z databázy zo všetkých objektov v Orders, zobrať všetky a dať do premennej orders
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers':customers,
                'total_orders':total_orders, 'delivered':delivered, 'pending':pending
    }  # dictionary s ľubovoľným množstvom prvkov

    return render(request, 'accounts/dashboard.html', context)  # tu vytvorené prvky z premennej context použijeme v templates/products.py a templates/status.py

def products(request):
    products = Product.objects.all()  # z databázy Produktov vybrať všetko a uložiť do premennej products

    return render(request, 'accounts/products.html', {'products': products})  # tu vytvorené 'products' použijeme v templates/products.py

def customers(request):
    return render(request, 'accounts/customer.html')

  