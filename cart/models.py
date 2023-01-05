from django.db import models
from catalog.models import Product
from django.contrib.auth.models import User
from django.utils import timezone


# Статус товару
class StatusCartItem(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Статус')

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Статуси'


# Інформація про товар у кошику
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Користувач')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    date = models.DateTimeField(null=False, default=timezone.now, verbose_name='Дата додавання у кошик')
    status = models.CharField(max_length=100, verbose_name='Статус')
    # TODO
    # status = models.ForeignKey(StatusCartItem, on_delete=models.CASCADE, verbose_name='Статус')

    def __str__(self) -> str:
        return f'{self.user} / {self.product} :: {self.date} -> ({self.status})'

    class Meta:
        verbose_name_plural = 'Товари в кошику'
        verbose_name = 'Замовлення'

