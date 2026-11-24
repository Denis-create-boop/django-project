from django.urls import path
from . import views
urlpatterns = [
    path('', views.tv_home, name='tv_home'),
    path('create_tv', views.create_tv, name='create_tv'),
    path('<int:pk>', views.product_detail, name='tv-detail'),
    path('<int:pk>/update', views.product_update, name='tv-update'),
    path('<int:pk>/delete', views.product_delete, name='tv-delete'),
]
