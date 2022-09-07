from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('shorten/', views.makeshorturl),
    path('<str:shorturl>', views.redirectUrl)
]