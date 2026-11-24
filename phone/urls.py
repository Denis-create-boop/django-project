from django.urls import path
from . import views
urlpatterns = [
    path('', views.phone_home, name='phone_home'),
    path('create_phone', views.create_phone, name='create_phone'),
    path('<int:pk>', views.product_detail, name='phone-detail'),
    path('<int:pk>/update', views.product_update, name='phone-update'),
    path('<int:pk>/delete', views.product_delete, name='phone-delete'),
]
