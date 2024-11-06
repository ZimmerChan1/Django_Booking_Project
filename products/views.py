from django.shortcuts import render, get_object_or_404
from products.models import ProductCategory, Product, ProductReview  # Добавьте ProductReview


# Главная страница
def start_page(request):
    return render(request, "products/start_page.html")


# Страница индекса
def index(request):
    return render(request, "products/index.html")


# Каталог продуктов
def products(request):
    context = {
        "title": "каталог",
        "categories": ProductCategory.objects.all(),
        "products": Product.objects.all(),
    }
    return render(request, "products/products.html", context)


# Детали продукта и отзывы
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Получаем продукт по его первичному ключу
    reviews = product.reviews.all()  # Получаем все отзывы для данного продукта

    context = {
        "product": product,
        "reviews": reviews,  # Передаем отзывы в шаблон
    }
    return render(request, "products/product_detail.html", context)
