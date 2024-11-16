from django.urls import path
from MainApp import views

urlpatterns = [
    path("", views.home , name = "home"),
    path("signup/", views.signup , name = "signup"),
    path("login/", views.loginUser , name = "login"),
    path("attendances/", views.attendances, name = "attendances"),
]
