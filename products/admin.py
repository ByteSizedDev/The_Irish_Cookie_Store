from django.contrib import admin
from .models import Product, Category, FlavourImage, Flavour

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class FlavourImageInline(admin.StackedInline):
    max_num = 2
    model = FlavourImage

class FlavourAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'name',
    )
    inlines = (
        FlavourImageInline,
    )



admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Flavour, FlavourAdmin)