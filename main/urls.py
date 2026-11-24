from django.urls import path
from django.contrib.auth import views as auth_views
from . import views, cart

urlpatterns = [
    path('cart/', cart.view, name='cart'),
    path('cart/add/<str:category>/<int:pk>/', cart.add, name='cart_add'),
    path('cart/change/<str:category>/<int:pk>/', cart.change, name='cart_change'),
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('add/', views.add, name='add'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('manage/', views.dashboard, name='dashboard'),
]
