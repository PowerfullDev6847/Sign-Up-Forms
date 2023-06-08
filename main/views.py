from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse,HttpResponseRedirect
from .forms import OrderForm

def add_order(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "main/add_order.html", {"form":form})