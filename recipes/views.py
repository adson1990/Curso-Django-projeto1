from django.http import HttpResponse
from django.shortcuts import render
from seed import make_recipe

# Create your views here.

def home(request):
    return render(request, 'global/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(9)]
    })

def about(request):
    return HttpResponse('Sobre a aplicação!')

def contact(request):
    return HttpResponse('Página de contato!')

def recipe(request, id):
    return render(request, 'global/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        "is_detail_page": True
    })