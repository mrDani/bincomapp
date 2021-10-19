from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('/results', views.result, name="result"),

]
