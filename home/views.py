from django.shortcuts import render
from util.recipes.factory import make_recipe

# Create your views here.
def home(request):

    context = {
        'recipes': [make_recipe() for _ in range(10)],
    }

    return render(request,'home/pages/home.html',context=context)


def recipe(request,id):

    context = {
        'recipe': make_recipe
    }

    return render(request,'home/pages/recipe-view.html', context)