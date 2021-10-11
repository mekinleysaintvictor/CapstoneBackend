from django.urls import path
from musicians import views

urlpatterns = [
    # path('', views.MusicianList.as_view())
    path('all/', views.get_all_musicians)
]