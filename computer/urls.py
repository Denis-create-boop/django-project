from django.urls import path
from . import views
urlpatterns = [
    path('', views.comp_home, name='comp_home'),
    path('create_computer', views.create_computer, name='create_computer'),
    path('<int:pk>', views.product_detail, name='comp-detail'),
    path('<int:pk>/update', views.product_update, name='comp-update'),
    path('<int:pk>/delete', views.product_delete, name='comp-delete'),
]
