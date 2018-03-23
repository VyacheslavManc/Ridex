from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html', {})


def reviews(request):
    return render_to_response('reviews.html', {})


def support(request):
    return render_to_response('supportnoavtoris.html', {})