from django.urls import path,include
from . import views

urlpatterns = [
    path('login/', views.loginPage, name = "home"),
    path('secret/', views.secretPage, name = "secret"),
    path('logout', views.logout, name = "logout")
]