from django.shortcuts import render
from .forms import BookForm



def index(request):
    return render(request, "blog/index.html")

def add_book(request):
    form = BookForm()
    return render(request, "blog/create.html", {"form":form})