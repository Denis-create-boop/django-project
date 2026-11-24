from django.db import models
from main.catalog import ProductFields, image_path

class Condition(ProductFields):
    title = models.CharField('Название', max_length=50)
    model = models.CharField('Модель', max_length=50)
    full_text = models.TextField('Описание')
    date = models.DateTimeField('Дата добавления')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/conditioner/{self.id}'

    class Meta:
        verbose_name = 'кондиционер'
        verbose_name_plural = 'кондиционеры'

class ConditionImage(models.Model):
    product = models.ForeignKey(Condition, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('Фото', upload_to=image_path)
    class Meta:
        ordering = ['id']
        verbose_name = 'фотография'
        verbose_name_plural = 'фотографии'
