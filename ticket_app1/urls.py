from ticket_app1 import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name="add"),
    path('update/<int:pk>/', views.update, name="update"),
    path('deleteorder/<int:pk>/', views.deleteorder, name="deleteorder"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('details/<int:pk>/', views.details, name="details"),
]