from django.urls import path
from .views import index, add_book

urlpatterns = [
    path('', index, name='index'),
    path('add/book/', add_book, name="add_book")
]
