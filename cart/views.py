from django.shortcuts import render
from django.http.response import JsonResponse
from .models import *


def ajax_cart(request):
    response = dict()

    # 1 - Отримуємо значення GET параметрів з AJAX-запиту:
    userId = request.GET.get('userId')
    productId = request.GET.get('productId')

    # 2 - Зберігаємо товар, доданий до кошика, у БД:

    CartItem.objects.create(
        user_id=userId,
        product_id=productId,
        status='Очікування'
    )

    response['message'] = 'Товар збережено'

    # 3 - Зчитуємо з БД список всіх товарів даного користувача:
    user_items = CartItem.objects.filter(user_id=userId)

    # 4 - Обчислюємо загальну вартість всіх товарів даного користувача:
    amount = 0
    for item in user_items:
        amount += item.product.price

    # 5 - Записуємо у відповідь сервера загальну кількість та вартість товарів даного користувача:
    response['count'] = len(user_items)
    response['amount'] = amount

    return JsonResponse(response)
