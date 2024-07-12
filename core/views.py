from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request, "core/index.html")

def receta(request):
    return render(request, "core/receta.html")

def nosotros(request):
    return render(request, "core/nosotros.html")

def contacto(request):
    return render(request, "core/contacto.html")
