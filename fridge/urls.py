from django.urls import path
from . import views


urlpatterns = [
    path('', views.fridge_home, name='fridge_home'),
    path('create_fridge', views.create_fridge, name='create_fridge'),
    path('<int:pk>', views.FridgeDetailView.as_view(), name='fridge-detail'),
    path('<int:pk>/update', views.FridgeUpdateView.as_view(), name='fridge-update'),
    path('<int:pk>/delete', views.FridgeDeleteView.as_view(), name='fridge-delete'),
]