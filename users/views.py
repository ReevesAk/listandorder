from decouple import config

from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SignUpSerializer, StockUpScheduleSerializer
from .tokens import create_jwt_pair_for_user
from .models import StockUpSchedule
from .utils import send_email

# Create your views here.

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            sender = config('EMAIL_HOST_USER')
            app_password = config('EMAIL_HOST_PASSWORD')
            mail_data = {
                "email": [request.data.get("email")],
                "subject":  "Verify your Email",
                "body": "Use this OTP to verify your account",
                "sender": sender,
                "password": app_password,
            }
            
            send_email(
                subject=mail_data["subject"],
                body=mail_data["body"],
                sender=mail_data["sender"],
                recipients=mail_data["email"],
                password=mail_data["password"]
            )

            response = {"message": "User Created Successfully. An OTP has been sent to you mail for verification", "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = []

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:

            tokens = create_jwt_pair_for_user(user)

            response = {"message": "Login Successfull", "tokens": tokens}
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={"message": "Invalid email or password"})

    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)
    


class CreateStockUpSchedule(generics.CreateAPIView):
    queryset = StockUpSchedule.objects.all()
    serializer_class = StockUpScheduleSerializer


class DeleteStockUpSchedule(generics.DestroyAPIView):
    queryset = StockUpSchedule.objects.all()
    serializer_class = StockUpScheduleSerializer


class UpdateStockUpSchedule(generics.UpdateAPIView):
    queryset = StockUpSchedule.objects.all()
    serializer_class = StockUpScheduleSerializer