from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='site-home'),
    path('about/', views.about, name='site-about'),
    path('original/', views.original, name='site-original'),
    path('eastern/', views.eastern, name='site-eastern'),
    path('western/', views.western, name='site-western'),
    path('future/', views.future, name='site-future'),
    path('big/', views.big, name='site-big'),
    path('new/', views.new, name='site-new')
]
