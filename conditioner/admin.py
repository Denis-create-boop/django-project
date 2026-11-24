from django.contrib import admin
from .models import Condition, ConditionImage

class PhotoInline(admin.TabularInline):
    model = ConditionImage
    extra = 2

@admin.register(Condition)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','model','price','discount')
    inlines = [PhotoInline]
