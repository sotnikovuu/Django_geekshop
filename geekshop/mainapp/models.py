from django.db import models


class ProductCategory(models.Model):
    objects = None
    name = models.TextField(verbose_name='имя категории', max_length=64, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    href = 'products_'
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE
    )
    name = models.TextField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    short_desc = models.CharField(
        verbose_name='короткое описание',
        max_length=60,
        blank=True
    )
    description = models.TextField(verbose_name='Описание', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    def __str__(self):
        return f'{self.name} ({self.category.name})'

