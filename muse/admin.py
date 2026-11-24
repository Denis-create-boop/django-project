from django.contrib import admin
from .models import Muse, MuseImage

class PhotoInline(admin.TabularInline):
    model = MuseImage
    extra = 2

@admin.register(Muse)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','model','price','discount')
    inlines = [PhotoInline]
