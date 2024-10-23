from django.contrib import admin

from products.models import ProductCategory, Product

# Register your models here.


admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category")
    fields = ("name", "image", "description", "short_description", ("price", "category"))