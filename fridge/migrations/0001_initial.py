# Generated by Django 5.0.4 on 2024-05-14 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fridge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('model', models.CharField(max_length=50, verbose_name='Модель')),
                ('full_text', models.TextField(verbose_name='Описание')),
                ('date', models.DateTimeField(verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'холодильник',
                'verbose_name_plural': 'холодильники',
            },
        ),
    ]
