from django.contrib import admin
from .models import Wash, WashImage

class PhotoInline(admin.TabularInline):
    model = WashImage
    extra = 2

@admin.register(Wash)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','model','price','discount')
    inlines = [PhotoInline]
