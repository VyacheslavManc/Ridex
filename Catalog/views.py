from django.shortcuts import render
from django.shortcuts import render_to_response
from Catalog.models import *


def catalog(request):
    context = {'category': Category.objects.all()}
    return render_to_response('category.html', context)
