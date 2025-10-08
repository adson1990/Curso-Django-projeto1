from django.contrib import admin
from .models import Category, Recipe

# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe)
   
class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
