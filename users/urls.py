from django.urls import path
from .views import (
    SignUp, Login, 
    CreateStockUpSchedule, DeleteStockUpSchedule, 
    UpdateStockUpSchedule, MyTokenObtainPairView
)    

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

 
urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('sign_up/', SignUp .as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('create_stock_up/', CreateStockUpSchedule.as_view(), name='create_stock_up'),
    path('update_stock_up/', UpdateStockUpSchedule.as_view(), name='update_stock_up'),
    path('remove_stock_up/', DeleteStockUpSchedule.as_view(), name='remove_stock_up')
]