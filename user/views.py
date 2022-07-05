from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def add(request):
    return HttpResponse("hello")

def wel(request):
    return render(request,"user/login.html")

def home(request):
    return render(request,'user/home.html')