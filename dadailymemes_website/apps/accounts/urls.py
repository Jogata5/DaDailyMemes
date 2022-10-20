from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name="account"
urlpatterns = [
    path("profile", views.ProfileView.as_view(), name="profile"),

    path("signin", auth_views.LoginView.as_view(template_name="signin.html"), name="signin"),

    path("signup", auth_views.LoginView.as_view(template_name="signup.html"), name="signup"),

    path("quiz",auth_views.LoginView.as_view(template_name="quiz,html"), name="quiz"),

    path("signout", auth_views.LogoutView.as_view(), name = "signout"),
]