from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='my_app-login'),
    path('logout/', views.user_logout, name='my_app-logout'),
    path('register/', views.signup, name='my_app-register'),
    path('view_all/', views.view_all, name='view-all'),
    path('postAd', views.post_ad, name='post-ad'),
    path('calculate_price/', views.calculate_price, name='calculate-price'),
]
