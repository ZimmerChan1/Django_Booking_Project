from django.contrib import admin

from products.models import ProductCategory, Product, ProductReview

# Register your models here.


admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "city", "lease_duration", "pets_allowed")
    fields = (
        "name",
        "image",
        "description",
        "short_description",
        ("price", "category"),
        "city",
        "lease_duration",
        "pets_allowed"
    )
    list_filter = ("category", "city", "lease_duration", "pets_allowed")
    search_fields = ("name", "city", "description")

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'repair', 'neighbors', 'area', 'furniture_condition')
    search_fields = ('product__name', 'user__username')