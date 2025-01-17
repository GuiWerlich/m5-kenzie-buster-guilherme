from django.urls import path
from rest_framework_simplejwt import views
from .views import UserView, LoginJWTView

urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/<int:user_id>/', UserView.as_view()),
    path("users/login/", LoginJWTView.as_view()), 
    path("token/refresh/", views.TokenRefreshView.as_view())
]