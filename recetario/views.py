from django.shortcuts import render
from .models import Receta

# Create your views here.
def index(request):
    recetas = Receta.objects.all()
    return render(request, 'recetario/index.html',{'recetas':recetas})