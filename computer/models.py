from django.db import models
from main.catalog import ProductFields, image_path

class Computer(ProductFields):
    title = models.CharField('Название', max_length=50)
    model = models.CharField('Модель', max_length=50)
    full_text = models.TextField('Описание')
    date = models.DateTimeField('Дата добавления')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/computer/{self.id}'

    class Meta:
        verbose_name = 'компьютер'
        verbose_name_plural = 'компьютеры'

class ComputerImage(models.Model):
    product = models.ForeignKey(Computer, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('Фото', upload_to=image_path)
    class Meta:
        ordering = ['id']
        verbose_name = 'фотография'
        verbose_name_plural = 'фотографии'
