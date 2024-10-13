from django.urls import path
from . import views


urlpatterns = [
    path('', views.conditioner_home, name='conditioner_home'),
    path('create_condition', views.create_condition, name='create_condition'),
    path('<int:pk>', views.ConditionerDetailView.as_view(), name='condition-detail'),
    path('<int:pk>/update', views.ConditionerUpdateView.as_view(), name='condition-update'),
    path('<int:pk>/delete', views.ConditionerDeleteView.as_view(), name='condition-delete'),
]