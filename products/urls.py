from django.urls import path
from products.views import products, product_detail  # Импортируйте ваше новое представление

app_name = "products"

urlpatterns = [
    path('', products, name='index'),
    path('products/', products, name='products'),  # Добавлен слеш в конце для соответствия стандартам
    path('product/<int:pk>/', product_detail, name='product_detail'),  # Новый маршрут
]
