from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name="account"
urlpatterns = [
    path("profile", views.ProfileView.as_view(), name="profile"),

    path("profile_update", views.profile_update , name="profile_update"),

    path('signin_user', auth_views.LoginView.as_view(template_name="signin.html"), name="signin"),

    path('signup_user', views.signup_user , name="signup"),

    path('sign_user', auth_views.LogoutView.as_view(), name = "signout"),

    path('timer', views.timer , name ="timer" ),
]