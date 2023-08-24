from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from apps.users.views import RegistrationView
urlpatterns = [
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path(
        "token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("registration/", RegistrationView.as_view(), name="user_register"),

]
