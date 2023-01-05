from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'amount', 'category', 'color', 'type_product', 'material')
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(CategoryProduct, CategoryAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(ColorProduct, ColorAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(TypeProduct, TypeAdmin)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(MaterialProduct, MaterialAdmin)
