from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name="account"
urlpatterns = [
    path("profile", views.ProfileView.as_view(), name="profile"),

    path("signin", auth_views.LoginView.as_view(template_name="signin.html"), name="signin"),

    path("signup", auth_views.LogoutView.as_view(), name="signup"),
    # path("admin/", admin.site.urls),
    # path("", include("DaDailyMemes_website.apps.accounts.urls")),
    # path('accounts/', include("DaDailyMemes_website.apps.accounts.urls"))
    
]