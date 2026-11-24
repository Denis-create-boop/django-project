from django.urls import path
from . import views
urlpatterns = [
    path('', views.muse_home, name='muse_home'),
    path('create_muse', views.create_muse, name='create_muse'),
    path('<int:pk>', views.product_detail, name='muse-detail'),
    path('<int:pk>/update', views.product_update, name='muse-update'),
    path('<int:pk>/delete', views.product_delete, name='muse-delete'),
]
