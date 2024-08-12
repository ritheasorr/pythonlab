from django.urls import path

from . import views

urlpatterns = [
    path('', views.loginView, name='login'),
    path('home/', views.index, name='index'),
    # path('', views.index, name='index'),
    path('login/', views.loginView, name='login'),
    path('register/', views.registerView, name='register'),
]
