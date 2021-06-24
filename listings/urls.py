from django.urls import path

from . import views

urlpatterns = [
    path('', views.show, name='listings'),
    path('listing', views.listing, name='listing'),
    path('createitem', views.listing, name='createitem'),
    path('listing/<int:id>', views.delete),    
    path('editdb/emp', views.emp),  


]