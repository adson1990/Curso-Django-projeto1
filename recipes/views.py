from django.http import HttpResponse
from django.shortcuts import render
from seed import make_recipe
from .models import Recipe

# Create your views here.

def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')[:9]
    return render(request, 'global/pages/home.html', context={
       # 'recipes': [make_recipe() for _ in range(9)]
        'recipes': recipes
    })

def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    return render(request, 'global/pages/category.html', context={
       # 'recipes': [make_recipe() for _ in range(9)]
        'recipes': recipes
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