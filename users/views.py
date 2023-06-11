from django.shortcuts import get_object_or_404


# Third party imports.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# In project imports.
from .serializers import SignUpSerializer, LoginSerializer, StockUpScheduleSerializer
from .models import User, StockUpSchedule


# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


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


class CreateStockUpSchedule(generics.CreateAPIView):
    queryset = StockUpSchedule.objects.all()
    serializer_class = StockUpScheduleSerializer


class DeleteStockUpSchedule(generics.DestroyAPIView):
    queryset = StockUpSchedule.objects.all()
    serializer_class = StockUpScheduleSerializer


class UpdateStockUpSchedule(generics.UpdateAPIView):
    queryset = StockUpSchedule.objects.all()
    serializer_class = StockUpScheduleSerializer