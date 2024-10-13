from django.urls import path
from . import views


urlpatterns = [
    path('', views.comp_home, name='comp_home'),
    path('create_computer', views.create_computer, name='create_computer'),
    path('<int:pk>', views.ComputerDetailView.as_view(), name='comp-detail'),
    path('<int:pk>/update', views.ComputerUpdateView.as_view(), name='comp-update'),
    path('<int:pk>/delete', views.ComputerDeleteView.as_view(), name='comp-delete'),
]