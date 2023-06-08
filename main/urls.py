from django.urls import path
from .views import add_order

urlpatterns = [
    path('add/order/', add_order, name="add_order")
]
  