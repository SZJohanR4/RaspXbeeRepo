from django.http import HttpResponse
from django.shortcuts import render
from .forms import loginForm

def index(request):
    return render(request,'index.html',{"form":loginForm})

def conexiones(request):
    return render(request,'conexionEthernet.html')
