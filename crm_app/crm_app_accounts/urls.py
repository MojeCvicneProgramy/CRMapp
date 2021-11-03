from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    # ťahá funkciu products zo súboru views v tej istej zložke
    path('produkty', views.products),
    # ťahá funkciu customers zadefimńovanú v súbore views v tej istej zložke
    path('zakaznici/<str:pk_test>/', views.customers),
]
