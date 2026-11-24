from django.db import models
from main.catalog import ProductFields, image_path

class Fridge(ProductFields):
    title = models.CharField('Название', max_length=50)
    model = models.CharField('Модель', max_length=50)
    full_text = models.TextField('Описание')
    date = models.DateTimeField('Дата добавления')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/fridge/{self.id}'

    class Meta:
        verbose_name = 'холодильник'
        verbose_name_plural = 'холодильники'

class FridgeImage(models.Model):
    product = models.ForeignKey(Fridge, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('Фото', upload_to=image_path)
    class Meta:
        ordering = ['id']
        verbose_name = 'фотография'
        verbose_name_plural = 'фотографии'
