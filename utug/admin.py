from django.contrib import admin
from .models import Utug, UtugImage

class PhotoInline(admin.TabularInline):
    model = UtugImage
    extra = 2

@admin.register(Utug)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','model','price','discount')
    inlines = [PhotoInline]
