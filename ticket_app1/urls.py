from ticket_app1 import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
]