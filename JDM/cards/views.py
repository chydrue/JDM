from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, '/home/zero/Documentos/Web/JDM/JDM/cards/templates/index.html')