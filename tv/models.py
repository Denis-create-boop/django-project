from django.db import models

# Create your models here.
class Tv(models.Model):
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