"""crm_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# include umožní natiahnuť urls aj z inej zložky - z našej aplikácie crm_app_acounts

urlpatterns = [
    path('admin/', admin.site.urls),  # bolo prednastavené
    path('', include('crm_app_accounts.urls'))  # všetko okrem admin stránky natiahne z aplikácie crm_app_account

]
