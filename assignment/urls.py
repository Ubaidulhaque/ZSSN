from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('survivors/', views.all_survivors),
    path('survivors/<str:id>', views.update_survivor),
]