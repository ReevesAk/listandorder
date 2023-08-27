from django.urls import path
from .views import (
    SignUpView, LoginView, VerifyOTP,
    CreateStockUpSchedule, DeleteStockUpSchedule, 
    UpdateStockUpSchedule, SendMail, Logout
)    

from rest_framework_simplejwt.views import (
    TokenRefreshView, TokenVerifyView, TokenObtainPairView
)
 
urlpatterns = [
    # auth endpoints.
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("verify-email/", VerifyOTP.as_view(), name="email_verify"),
    path("logout/", Logout.as_view(), name="logout"),

    # token enpoints.
    path("token/create", TokenObtainPairView.as_view(), name="token_create"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),

    # Stock up endpoints.
    path("create-stock_up/<int:id>/", CreateStockUpSchedule.as_view(), name='create_stock_up'),
    path("update-stock_up/<int:id>/", UpdateStockUpSchedule.as_view(), name='update_stock_up'),
    path("remove-stock_up/<int:pk>/", DeleteStockUpSchedule.as_view(), name='remove_stock_up'),

    # Utility endpoints.
    path("send-mail/", SendMail.as_view(), name='sendmail')
]
