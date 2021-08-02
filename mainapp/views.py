from django.shortcuts import render

from mainapp.models import Product

from mainapp.models import ProductCategory


def index(request):
    title = 'каталог'

    # links_menu = [
    #     {'href': 'index', 'name': 'все'},
    #     {'href': 'products_home', 'name': 'дом'},
    #     {'href': 'products_office', 'name': 'офис'},
    #     {'href': 'products_modern', 'name': 'модерн'},
    #     {'href': 'products_classic', 'name': 'классика'},
    # ]

    products = Product.objects.all()[:4]
    categories = ProductCategory.objects.all()


    context ={
        'title': title,
        #'links_menu': links_menu,
        'realeted_products': products,
        'links_menu': categories,
    }
    return render(request, 'mainapp/products.html', context)
