from django.shortcuts import render
from django.shortcuts import render_to_response
from Catalog.models import *


def cat(request):
    return render_to_response('accaunts.html', {'category': Category})
