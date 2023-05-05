from django.shortcuts import render, redirect
from .forms import BookForm, WebUserForm
from .models import WebUser


def index(request):
    web_users = WebUser.objects.all()
    return render(request, "blog/index.html",{"users": web_users})

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
