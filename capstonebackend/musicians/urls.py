from django.urls import path
from musicians import views

urlpatterns = [
    path('all/', views.get_all_musicians),
    path('user/', views.get_one_musician),
    path('<int:pk>/', views.get_details),
    path('<int:pk>/', views.get_one_other_musician),
    path('<int:pk>/friend/', views.friend_request),
    path('<int:pk>/deleterequest/', views.delete_request),
    path('', views.user_profiles),
]