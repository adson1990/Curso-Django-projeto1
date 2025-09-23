from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'global/pages/home.html', context={
        'name':'Adson Farias'
    })

def about(request):
    return HttpResponse('Sobre a aplicação!')

def contact(request):
    return HttpResponse('Página de contato!')

def recipe(request, id):
    return render(request, 'global/pages/recipe-view.html', context={
        'name':'Testando novas urls'
    })

def recipe_detail(request, id):
    # Futuramente buscar pelo ID no banco ex: Recipe.objects.get(pk=id)
    return render(request, 'recipes/recipe-view.html', {
        'id': id
    })