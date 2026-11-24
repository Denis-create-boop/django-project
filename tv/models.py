from django.db import models
from main.catalog import ProductFields, image_path

class Tv(ProductFields):
    title = models.CharField('Название', max_length=50)
    model = models.CharField('Модель', max_length=50)
    full_text = models.TextField('Описание')
    date = models.DateTimeField('Дата добавления')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/tv/{self.id}'

    class Meta:
        verbose_name = 'телевизор'
        verbose_name_plural = 'телевизоры'

class TvImage(models.Model):
    product = models.ForeignKey(Tv, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('Фото', upload_to=image_path)
    class Meta:
        ordering = ['id']
        verbose_name = 'фотография'
        verbose_name_plural = 'фотографии'
