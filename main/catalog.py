from decimal import Decimal, ROUND_HALF_UP
from uuid import uuid4
from pathlib import Path
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

def image_path(instance, filename):
    return f'products/{uuid4().hex}{Path(filename).suffix.lower()}'

class ProductFields(models.Model):
    price = models.DecimalField('Цена', max_digits=12, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(Decimal('0.01'))])
    discount = models.PositiveSmallIntegerField('Скидка, %', default=0, validators=[MaxValueValidator(100)])
    specifications = models.JSONField('Характеристики', default=dict, blank=True)
    class Meta:
        abstract = True

    @property
    def final_price(self):
        if self.price is None:
            return None
        return (self.price * (Decimal(100) - self.discount) / 100).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    @property
    def cover(self):
        return next(iter(self.images.all()), None)

CATEGORIES = {
    'tv': {'model': 'Tv', 'prefix': 'tv', 'home': 'tv_home', 'create': 'create_tv', 'label': 'Телевизоры', 'specs': ["Диагональ экрана","Разрешение","Тип матрицы","Частота обновления","Smart TV","HDMI"]},
    'muse': {'model': 'Muse', 'prefix': 'muse', 'home': 'muse_home', 'create': 'create_muse', 'label': 'Акустика', 'specs': ["Тип акустики","Мощность","Количество каналов","Частотный диапазон","Bluetooth","Подключение"]},
    'computer': {'model': 'Computer', 'prefix': 'comp', 'home': 'comp_home', 'create': 'create_computer', 'label': 'Компьютеры', 'specs': ["Процессор","Оперативная память","Видеокарта","Накопитель","Операционная система","Тип корпуса"]},
    'fridge': {'model': 'Fridge', 'prefix': 'fridge', 'home': 'fridge_home', 'create': 'create_fridge', 'label': 'Холодильники', 'specs': ["Общий объём","Объём морозильника","Класс энергопотребления","Размораживание","Уровень шума","Габариты"]},
    'wash': {'model': 'Wash', 'prefix': 'wash', 'home': 'wash_home', 'create': 'create_wash', 'label': 'Стиральные машины', 'specs': ["Загрузка","Тип загрузки","Скорость отжима","Класс энергопотребления","Программы","Габариты"]},
    'conditioner': {'model': 'Condition', 'prefix': 'condition', 'home': 'conditioner_home', 'create': 'create_condition', 'label': 'Кондиционеры', 'specs': ["Тип","Площадь помещения","Мощность охлаждения","Инвертор","Уровень шума","Класс энергопотребления"]},
    'utug': {'model': 'Utug', 'prefix': 'utug', 'home': 'utug_home', 'create': 'create_utug', 'label': 'Утюги', 'specs': ["Мощность","Материал подошвы","Подача пара","Паровой удар","Объём резервуара","Автоотключение"]},
    'phone': {'model': 'Phone', 'prefix': 'phone', 'home': 'phone_home', 'create': 'create_phone', 'label': 'Телефоны', 'specs': ["Диагональ экрана","Процессор","Оперативная память","Встроенная память","Камера","Ёмкость аккумулятора","Операционная система"]},
}

def product_model(category):
    from django.apps import apps
    return apps.get_model(category, CATEGORIES[category]['model'])
