from django.shortcuts import render

# Third party imports.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

# In_project imports
from . serializers import CheckoutSerializers
from .models import Checkout

# Create your views here.
class CreateCheckoutPage(generics.CreateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializers
