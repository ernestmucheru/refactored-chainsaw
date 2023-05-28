from django.contrib import admin
from django.urls import path
from tours import views

urlpatterns = [

    #Home
    path('', views.home, name="home"),
    #Add Tour
    path('add_tour', views.add_tour, name="add_tour"),
    #Edit Tour
    path('edit_tour', views.edit_tour, name="edit_tour"),
    #View Tour Individually
    path('tour/<str:tour_id>', views.tour, name="tour"),
    #Delete Tour
    path('delete_tour/<str:tour_id>', views.delete_tour, name="delete_tour"),


]