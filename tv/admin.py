from django.contrib import admin
from .models import Tv, TvImage

class PhotoInline(admin.TabularInline):
    model = TvImage
    extra = 2

@admin.register(Tv)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','model','price','discount')
    inlines = [PhotoInline]
