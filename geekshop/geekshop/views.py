from django.shortcuts import render

from mainapp.models import Product


def index(request):
    title = 'GeekShop'
    products = Product.objects.all()[:2]

    context = {
        'title' : title,
        'products' : products,
    }
    return render(request, 'geekshop/index.html', context)

def contacts(request):
    title = 'Контакты'
    context = {
        'title' : title,
    }
    return render(request, 'geekshop/contact.html', context)