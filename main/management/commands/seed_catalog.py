import json
from pathlib import Path
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from main.catalog import CATEGORIES, product_model
from main.demo_art import render_product

class Command(BaseCommand):
    help = 'Populate the catalog with 80 fictional demonstration products, without overwriting existing records.'

    def handle(self, *args, **options):
        data = json.loads(Path(__file__).with_name('demo_catalog.json').read_text(encoding='utf-8'))
        created = 0
        for category, rows in data.items():
            info = CATEGORIES[category]
            model = product_model(category)
            for i, (name, price, values) in enumerate(rows):
                specs = dict(zip(info['specs'], values.split('|'), strict=True))
                title = 'Eleck ' + name
                code = 'DEMO-' + category.upper() + '-' + str(i+1).zfill(2)
                description = (f'{title} — демонстрационная модель из раздела «{info["label"]}». '
                               + '. '.join(f'{key}: {value}' for key, value in list(specs.items())[:3])
                               + '. Подробные параметры приведены в характеристиках. '
                               + 'Цена и характеристики условные; изображение — иллюстрация.')
                with transaction.atomic():
                    product, new = model.objects.get_or_create(model=code, defaults={
                        'title':title, 'full_text':description, 'date':timezone.now(),
                        'price':price, 'discount':{1:10,4:15,7:20}.get(i,0),
                        'specifications':specs,
                    })
                    if new:
                        created += 1
                    if not product.images.exists():
                        for angle in (0, 1):
                            buffer = BytesIO()
                            render_product(category, i, angle).save(buffer, format='PNG')
                            photo = product.images.model(product=product)
                            photo.image.save(f'{code}-{angle}.png', ContentFile(buffer.getvalue()), save=True)
            self.stdout.write(f'{info["label"]}: {model.objects.count()} товаров')
        self.stdout.write(self.style.SUCCESS(f'Добавлено новых товаров: {created}.'))
