from django.http import HttpResponse
from django.shortcuts import render

from . import models


def index(request):
    res = models.Recipes.objects.all()

    return render(request, template_name='core/index.html', context={'res': res, 'title': 'Список рецептов'})
