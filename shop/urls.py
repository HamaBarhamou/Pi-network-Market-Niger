from django.urls import path
from . import views

urlpatterns = [
    path('newshop', views.updateshop, name="newshop"),
    path('dashbord', views.dashbord, name="dashbord"),
    path('mesboutique', views.mesboutique, name="mesboutique"),
]