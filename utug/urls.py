from django.urls import path
from . import views
urlpatterns = [
    path('', views.utug_home, name='utug_home'),
    path('create_utug', views.create_utug, name='create_utug'),
    path('<int:pk>', views.product_detail, name='utug-detail'),
    path('<int:pk>/update', views.product_update, name='utug-update'),
    path('<int:pk>/delete', views.product_delete, name='utug-delete'),
]
