from django.urls import path

from . import views

urlpatterns = [
    path('createitem', views.createItem, name='createitem'),

]