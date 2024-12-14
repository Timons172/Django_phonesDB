from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=30, verbose_name='Название модели')
    image = models.URLField(max_length=200, verbose_name='Изображение')
    price = models.IntegerField(verbose_name='Цена')
    release_date = models.DateField(verbose_name='Дата выхода')
    lte_exists = models.BooleanField(verbose_name='Наличие LTE')
    slug = models.SlugField(max_length=30, unique=True)
