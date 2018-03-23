from django.shortcuts import render


def order_verification(request):
    return render(request, 'checkorder.html', {})