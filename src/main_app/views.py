from django.shortcuts import render


def base_view(request):
    return render(request, 'main_app/index.html')


def products(request):
    return render(request, 'main_app/products.html')
