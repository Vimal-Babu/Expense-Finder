from django.shortcuts import render

# Create your views here.

def signup(request):
    print("signup view works from the new app")
    return render(request,'signup.html')


def login(request):
    print("loading login page from the new app")
    return render(request,'login.html')

def logout(request):
    print("loading logout page")
    return render(request,'home.html')
