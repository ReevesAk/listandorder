from django.shortcuts import get_object_or_404


# Third party imports.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

# In project imports.
from .serializers import SignUpSerializer, LoginSerializer
from .models import User


# Create your views here.

# Register handles the POST request of registering a user, It takes in 
# username, email and password and returns user details upon success.
class SignUp(generics.GenericAPIView):

    serializer_class = SignUpSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)
    


# LoginAPIView handles the POST request of logging in
# a registered user with valid login credentials.
class Login(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)