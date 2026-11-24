from django.contrib import admin
from .models import Fridge, FridgeImage

class PhotoInline(admin.TabularInline):
    model = FridgeImage
    extra = 2

@admin.register(Fridge)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','model','price','discount')
    inlines = [PhotoInline]
