from django.urls import path
from . import views


urlpatterns = [
    path('', views.phone_home, name='phone_home'),
    path('create_phone', views.create_phone, name='create_phone'),
    path('<int:pk>', views.PhoneDetailView.as_view(), name='phone-detail'),
    path('<int:pk>/update', views.PhoneUpdateView.as_view(), name='phone-update'),
    path('<int:pk>/delete', views.PhoneDeleteView.as_view(), name='phone-delete'),
]