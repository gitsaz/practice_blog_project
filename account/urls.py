from django.urls import path

from .views import(
    user_login,
    registration
)
urlpatterns = [
    path("user_login/", user_login, name="user_login"),
    path("registration/", registration, name="registration")
]