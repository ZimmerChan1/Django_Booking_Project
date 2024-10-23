from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404
from products.models import ProductCategory, Product


# Create your views here.

def start_page(request):
    return  render(request, "products/start_page.html")


def index(request):
    return render(request, "products/index.html")


# каталог
def products(request):
    context = {
        "title": "каталог",
        "categories": ProductCategory.objects.all(),
        "products": Product.objects.all(),
    }
    return render(request, "products/products.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Получите продукт по его первичному ключу
    context = {
        "product": product,
    }
    return render(request, "products/product_detail.html", context)
