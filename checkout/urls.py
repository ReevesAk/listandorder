from django.urls import path
from . views import *

urlpatterns = [
    path("create_checkout/", CreateCheckoutPage.as_view(), name="create_checkout"),
   
]