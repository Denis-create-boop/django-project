from django.urls import path
from . import views


urlpatterns = [
    path('', views.utug_home, name='utug_home'),
    path('create_utug', views.create_utug, name='create_utug'),
    path('<int:pk>', views.UtugDetailView.as_view(), name='utug-detail'),
    path('<int:pk>/update', views.UtugUpdateView.as_view(), name='utug-update'),
    path('<int:pk>delete', views.UtugDeleteView.as_view(), name='utug-delete'),
]