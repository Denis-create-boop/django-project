from django.urls import path
from . import views


urlpatterns = [
    path('', views.wash_home, name='wash_home'),
    path('create_wash', views.create_wash, name='create_wash'),
    path('<int:pk>', views.WashDetailView.as_view(), name='wash-detail'),
    path('<int:pk>/update', views.WashUpdateView.as_view(), name='wash-update'),
    path('<int:pk>/delete', views.WashDeleteView.as_view(), name='wash-delete'),
]