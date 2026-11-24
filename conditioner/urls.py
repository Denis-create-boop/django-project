from django.urls import path
from . import views
urlpatterns = [
    path('', views.conditioner_home, name='conditioner_home'),
    path('create_condition', views.create_condition, name='create_condition'),
    path('<int:pk>', views.product_detail, name='condition-detail'),
    path('<int:pk>/update', views.product_update, name='condition-update'),
    path('<int:pk>/delete', views.product_delete, name='condition-delete'),
]
