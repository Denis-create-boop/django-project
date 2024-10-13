from django.urls import path
from . import views


urlpatterns = [
    path('', views.tv_home, name='tv_home'),
    path('create_tv', views.create_tv, name='create_tv'),
    path('<int:pk>', views.TvDetailView.as_view(), name='tv-detail'),
    path('<int:pk>/update', views.TvUpdateView.as_view(), name='tv-update'),
    path('<int:pk>/delete', views.TvDeleteView.as_view(), name='tv-delete'),
]