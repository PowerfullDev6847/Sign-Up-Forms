from django.urls import path
from .views import index, add_book, add_user

urlpatterns = [
    path('', index, name='index'),
    path('add/book/', add_book, name="add_book"),
    path('add/user/', add_user, name = "add_user")
]
 