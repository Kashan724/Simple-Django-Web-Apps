

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"app1/index.html")
def kashan(request):
    return HttpResponse("Hi,Kashan")
def david(request):
    return HttpResponse("Hi,David")
def greet(request,name):
    return render(request,"app1/greet.html",{
        "name":name.capitaalize()
    })
