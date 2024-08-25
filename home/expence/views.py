from django.shortcuts import render
from .models import Main,PurchasedItem



def home(request):
    print("home is working loading the index page")
    return render(request,'home.html')


def expense(request):
    print("loading expence  page")
    return render(request,'expense.html')


def about(request):
    print("loading the about page")
    return render(request,'about.html')
