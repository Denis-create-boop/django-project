from django.urls import path
from . import views


urlpatterns = [
    path('', views.muse_home, name='muse_home'),
    path('create_muse', views.create_muse, name='create_muse'),
    path('<int:pk>', views.MuseDetailView.as_view(), name='muse-detail'),
    path('<int:pk>/update', views.MuseUpdateView.as_view(), name='muse-update'),
    path('<int:pk>/delete', views.MuseDeleteView.as_view(), name='muse-delete'),

]