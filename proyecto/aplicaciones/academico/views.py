from django.shortcuts import render
from .models import Materias

# Create your views here.

def home(request):
    MateriasListd = Materias.objects.all()
    return render(request, "index.html", {"Materias": MateriasListd})

