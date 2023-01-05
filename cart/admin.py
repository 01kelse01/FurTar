from django.contrib import admin
from .models import *


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'products', 'date', 'status')
    list_display_links = ('user',)


admin.site.register(CartItem)


class StatusCartItemAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(StatusCartItem)
