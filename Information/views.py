from django.shortcuts import render


def how_to_buy(request):
    return render(request, 'buy.html')
