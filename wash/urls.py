from django.urls import path
from . import views
urlpatterns = [
    path('', views.wash_home, name='wash_home'),
    path('create_wash', views.create_wash, name='create_wash'),
    path('<int:pk>', views.product_detail, name='wash-detail'),
    path('<int:pk>/update', views.product_update, name='wash-update'),
    path('<int:pk>/delete', views.product_delete, name='wash-delete'),
]
