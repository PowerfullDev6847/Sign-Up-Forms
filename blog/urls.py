from django.urls import path
from .views import index, add_book, add_user, delete_user, update_user

urlpatterns = [
    path('', index, name='index'),
    path('add/book/', add_book, name="add_book"),
    path('add/user/', add_user, name = "add_user"),
    path('update/<int:pk>/',update_user, name='update_user'),
    path('delete/<int:pk>/',delete_user, name='delete_user')
]
 