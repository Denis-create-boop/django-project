from django.contrib import admin
from .models import Computer, ComputerImage

class PhotoInline(admin.TabularInline):
    model = ComputerImage
    extra = 2

@admin.register(Computer)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','model','price','discount')
    inlines = [PhotoInline]
