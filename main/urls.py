from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('admin/', admin.site.urls, name='admin'),
    path('add/', views.add, name='add'),
]