from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("quiz/<int:pk>/", views.take_quiz, name="take"),
    path("quiz/<int:pk>/leaderboard/", views.leaderboard, name="leaderboard"),
    path("result/<int:pk>/", views.result, name="result"),
    path("my-results/", views.my_results, name="my_results"),
]
