from django.urls import path
from musicians import views

urlpatterns = [
    path('all/', views.get_all_musicians),
    path('', views.user_musicians)
]