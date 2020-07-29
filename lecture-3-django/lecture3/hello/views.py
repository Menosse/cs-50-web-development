from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render (request,"hello/index.html")

def returnName(request):
    return(HttpResponse("Hello, name!"))

def returnDog(request):
    return(HttpResponse("Hello, dog!"))

def returnCat(request):
    return(HttpResponse("Hello, cat!"))

def greet(request, greet_name):
    return render(request, "hello/greet.html",{
        "greet_name": greet_name.capitalize()
    })
