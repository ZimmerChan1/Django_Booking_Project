from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

#модель = таблица

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, primary_key=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='products_images', blank=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    # Новые поля с дефолтными значениями
    city = models.CharField(max_length=100, default="Не указан", verbose_name="Город")
    lease_duration = models.CharField(
        max_length=50,
        choices=[('short', 'Краткосрочная аренда'), ('long', 'Долгосрочная аренда')],
        default='short',  # Дефолтное значение
        verbose_name="Срок аренды"
    )
    pets_allowed = models.BooleanField(default=False, verbose_name="Можно с животными")

    def __str__(self):
        return self.name

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, '1 звезда'), (2, '2 звезды'), (3, '3 звезды')], verbose_name="Оценка")  # Оценка от 1 до 3
    repair = models.BooleanField(default=False, verbose_name="Ремонт")  # Наилучшая деталь: ремонт
    neighbors = models.BooleanField(default=False, verbose_name="Соседи")  # Наилучшая деталь: соседи
    area = models.BooleanField(default=False, verbose_name="Район")  # Наилучшая деталь: район
    furniture_condition = models.BooleanField(default=False, verbose_name="Состояние мебели и техники")  # Состояние мебели и техники
    comment = models.TextField(blank=True, verbose_name="Комментарий")  # Дополнительный комментарий пользователя
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата отзыва")  # Дата создания отзыва

    def __str__(self):
        return f"Отзыв от {self.user.username} для {self.product.name} - {self.rating} звезды"
