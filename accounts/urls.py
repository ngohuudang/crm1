from django.urls import path
from numpy import product
from . import views

urlpatterns = [
    path('',views.home),
    path('products/',views.products),
    path('customer/',views.customer)

]
