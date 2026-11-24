from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import django.core.validators
import main.catalog

class Migration(migrations.Migration):
    dependencies = [('computer', '0001_initial')]
    operations = [
        migrations.AddField(model_name='computer', name='price', field=models.DecimalField('Цена', max_digits=12, decimal_places=2, null=True, blank=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
        migrations.AddField(model_name='computer', name='discount', field=models.PositiveSmallIntegerField('Скидка, %', default=0, validators=[django.core.validators.MaxValueValidator(100)])),
        migrations.AddField(model_name='computer', name='specifications', field=models.JSONField('Характеристики', default=dict, blank=True)),
        migrations.CreateModel(name='ComputerImage', fields=[
            ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('image', models.ImageField('Фото', upload_to=main.catalog.image_path)),
            ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='computer.computer')),
        ], options={'ordering':['id'], 'verbose_name':'фотография', 'verbose_name_plural':'фотографии'}),
    ]
