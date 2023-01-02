from django.db import models


# Категорія товару
class CategoryProduct(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self) -> str:
        return str(self.name)


# Колір товару
class ColorProduct(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self) -> str:
        return str(self.name)


# Тип товару
class TypeProduct(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self) -> str:
        return str(self.name)


# Матеріал товару
class MaterialProduct(models.Model):
    name = models.CharField(max_length=150, unique=True, null=False)

    def __str__(self) -> str:
        return str(self.name)


# Товар
class Product(models.Model):
    name = models.CharField(max_length=150, null=False)
    about = models.TextField(max_length=500, null=False)
    photo = models.FileField(upload_to='photos/', null=False)
    price = models.FloatField(null=False)
    amount = models.IntegerField(null=False)
    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    color = models.ForeignKey(ColorProduct, on_delete=models.CASCADE)
    type_product = models.ForeignKey(TypeProduct, on_delete=models.CASCADE)
    material = models.ForeignKey(MaterialProduct,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.name)
