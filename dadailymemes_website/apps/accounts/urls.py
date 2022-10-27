from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name="account"
urlpatterns = [
#    path("profile", views.ProfileView.as_view(), name="profile"),

    path('signin_user', auth_views.LoginView.as_view(template_name="signin.html"), name="signin"),

    path('signup_user', auth_views.LoginView.as_view(template_name="signup.html"), name="signup"),

    path('signout_user', auth_views.LogoutView.as_view(), name = "signout"),
]