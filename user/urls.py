from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import BlacklistTokenView, CustomUserCreate

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("user/register/", CustomUserCreate.as_view(), name="create_user"),
    path("user/logout/blacklist/", BlacklistTokenView.as_view(), name="blacklist"),
]
