from django.db import models


# Категорія товару
class CategoryProduct(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, verbose_name='Категорія')

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Категорії'
        verbose_name = 'Категорія'


# Колір товару
class ColorProduct(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, verbose_name='Колір')

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Кольори'
        verbose_name = 'Колір'


# Тип товару
class TypeProduct(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, verbose_name='Тип виробу')

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Типи виробів'
        verbose_name = 'Тип виробу'


# Матеріал товару
class MaterialProduct(models.Model):
    name = models.CharField(max_length=150, unique=True, null=False, verbose_name='Матеріал виробу')

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Матеріали виробів'
        verbose_name = 'Матеріал виробу'


# Товар
class Product(models.Model):
    name = models.CharField(max_length=150, null=False, verbose_name='Назва товару')
    about = models.TextField(max_length=500, null=False, verbose_name='Опис товару')
    photo = models.FileField(upload_to='photos/', null=False, verbose_name='Фото товару')
    price = models.FloatField(null=False, verbose_name='Ціна товару')
    amount = models.IntegerField(null=False, verbose_name='Кількість')
    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Категорія')
    color = models.ForeignKey(ColorProduct, on_delete=models.CASCADE, verbose_name='Колір')
    type_product = models.ForeignKey(TypeProduct, on_delete=models.CASCADE, verbose_name='Тип')
    material = models.ForeignKey(MaterialProduct,on_delete=models.CASCADE, verbose_name='Матеріал')

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Товари'
