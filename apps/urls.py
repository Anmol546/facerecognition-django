from django.urls import path 
from apps import views

urlpatterns = [
    path('',views.index2,name='index2')
]