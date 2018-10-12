from django.http import HttpResponse
from django.shortcuts import render
from .forms import loginForm

def index(request):
    return render(request,'index.html',{"form":loginForm})

def conexiones(request):
    return render(request,'conexionEthernet.html')

def sistema(request):
    return render(request,'onOffSistema.html')

def red(request):
    return render(request,'infGetway.html')
