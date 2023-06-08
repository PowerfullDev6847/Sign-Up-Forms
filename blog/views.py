from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm, WebUserForm
from .models import WebUser
from main.models import Product, Category
from main.forms import ProductForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def index(request, cat_slug=None):
    q = request.GET.get('q')
    cats = Category.objects.all()
    if cat_slug:
        cat = get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category=cat)
    elif q:
        products = Product.objects.filter(
            Q(title__icontains=q) | Q(description__icontains=q)
        )
    else:
        products = Product.objects.all()
    return render(request, "blog/index.html",{"products": products, "cats": cats})

def product_detail(request, pk):
    product=get_object_or_404(Product, id=pk)
    return render(request, "blog/product_detail.html",{"product": product})


def add_product(request):
    form = ProductForm()
    if request.method=="POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, "main/add_product.html",{"form": form})


def add_book(request):
    form = BookForm()
    if request.method== "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect("index")
        else:
            print(form.errors)
    return render(request, "blog/create.html", {"form":form})




def add_user(request):
    form = WebUserForm()
    if request.method== "POST":
        form = WebUserForm(request.POST)
        if form.is_valid():
            WebUser.objects.create(
             full_name=form.cleaned_data.get('full_name'),
             email = form.cleaned_data.get('email'),
             username = form.cleaned_data.get('username'),
             password=form.cleaned_data.get('password'),
             show = form.cleaned_data.get('show')
            )
            return redirect('index')
    return render(request, "blog/create_user.html", {"form":form})


def update_user(request,pk):
    user = WebUser.objects.get(id=pk)
    form = WebUserForm(instance=user)
    if request.method =="POST":
        form = WebUserForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, "blog/update_user.html",{"form":form})



def delete_user(request,pk):
    user = WebUser.objects.get(id=pk)
    user.delete()
    return redirect('index')
