from django.contrib import admin
from .models import Phone, PhoneImage

class PhotoInline(admin.TabularInline):
    model = PhoneImage
    extra = 2

@admin.register(Phone)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','model','price','discount')
    inlines = [PhotoInline]
