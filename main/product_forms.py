from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .catalog import CATEGORIES

class MultipleImageInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleImageField(forms.ImageField):
    widget = MultipleImageInput
    def clean(self, data, initial=None):
        if not data:
            return []
        items = data if isinstance(data, (list, tuple)) else [data]
        if len(items) > 10:
            raise ValidationError('За один раз можно загрузить не более 10 фотографий.')
        cleaned = []
        for item in items:
            if item.size > 8 * 1024 * 1024:
                raise ValidationError('Максимальный размер фотографии — 8 МБ.')
            image = super().clean(item)
            if image.image.format not in ('JPEG', 'PNG', 'WEBP'):
                raise ValidationError('Допустимые форматы: JPEG, PNG, WebP.')
            # Use a verified extension, not the user-supplied filename.
            image.name = 'photo.' + {'JPEG':'jpg','PNG':'png','WEBP':'webp'}[image.image.format]
            cleaned.append(image)
        return cleaned

class ProductForm(forms.ModelForm):
    photos = MultipleImageField(label='Фотографии', required=False, help_text='Можно выбрать сразу несколько файлов (до 10, JPEG/PNG/WebP, до 8 МБ каждый).')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        category = self._meta.model._meta.app_label
        self.fields['price'].required = True
        self.fields['date'].required = False
        self.fields['date'].widget = forms.DateTimeInput(attrs={'type':'datetime-local'}, format='%Y-%m-%dT%H:%M')
        self.fields['date'].input_formats = ['%Y-%m-%dT%H:%M', '%Y-%m-%d %H:%M:%S']
        if not self.instance.pk:
            self.initial['date'] = timezone.localtime().strftime('%Y-%m-%dT%H:%M')
        for i, label in enumerate(CATEGORIES[category]['specs']):
            self.fields[f'spec_{i}'] = forms.CharField(label=label, required=False, max_length=200, initial=(self.instance.specifications or {}).get(label, ''))
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        self.fields['photos'].widget.attrs['accept'] = 'image/jpeg,image/png,image/webp'

    def clean_date(self):
        return self.cleaned_data.get('date') or timezone.now()

    def save(self, commit=True):
        obj = super().save(commit=False)
        labels = CATEGORIES[obj._meta.app_label]['specs']
        obj.specifications = {label: self.cleaned_data[f'spec_{i}'] for i, label in enumerate(labels) if self.cleaned_data.get(f'spec_{i}')}
        if commit:
            obj.save()
            self.save_m2m()
        return obj
