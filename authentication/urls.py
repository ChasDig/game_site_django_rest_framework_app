from django.urls import path

from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import CreateUserView, LogoutUserView

urlpatterns = [
    path('create/', CreateUserView.as_view()),
    path('login/', views.obtain_auth_token),
    path('logout/', LogoutUserView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
