from django.urls import path

from recipes.views import home, about, contact
from . import views


urlpatterns = [
    path('', home),
    path('sobre/', about),
    path('contato/', contact),  
    # PATH converter do Django. str -> string não vazia, aceita qualquer coisa que não seja uma barra
    # int -> números inteiros positivos
    # slug -> letras, números, underlines ou hifens
    # uuid -> aceita um UUID válido
    # path -> aceita qualquer coisa não vazia, inclusive barras
    path('recipe/<int:id>/', views.recipe, name='recipe-detail'),
]
