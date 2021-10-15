from django.urls import path
from musicians import views

urlpatterns = [
    path('all/', views.get_all_musicians),
    path('user/', views.get_one_musician),
    path('', views.user_profiles),
]