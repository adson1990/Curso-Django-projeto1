from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse('Sobre a aplicação!')

def contact(request):
    return HttpResponse('Página de contato!')