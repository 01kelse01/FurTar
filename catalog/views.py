from django.shortcuts import render
from .models import *


def index(request):
    all_products = Product.objects.all()
    all_category = CategoryProduct.objects.all()
    all_color = ColorProduct.objects.all()
    all_type = TypeProduct.objects.all()
    all_material = MaterialProduct.objects.all()
    return render(request, 'catalog/index.html', context={
        'title': 'Каталог товарів',
        'all_products': all_products,
        'all_category': all_category,
        'all_color': all_color,
        'all_type': all_type,
        'all_material': all_material,
    })
