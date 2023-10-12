from django.contrib.auth import views as auth_views
from django.urls import path

# from .views import user_login

urlpatterns = [
    # path("login/", user_login, name="user_login"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="ogout"),
]
