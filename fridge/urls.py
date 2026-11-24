from django.urls import path
from . import views
urlpatterns = [
    path('', views.fridge_home, name='fridge_home'),
    path('create_fridge', views.create_fridge, name='create_fridge'),
    path('<int:pk>', views.product_detail, name='fridge-detail'),
    path('<int:pk>/update', views.product_update, name='fridge-update'),
    path('<int:pk>/delete', views.product_delete, name='fridge-delete'),
]
