from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.validators import ValidationError

from users.models import User
from .models import ContactUs, Subscribe
from .serializers import (
    ContactUsSerializers, SubscribeSerializers
)


class ContactGraemart(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializers


class Subscribe(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SubscribeSerializers

    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            email = request.data.get("email")

            email_exists = User.objects.filter(email=email).exists()

            if not email_exists:
                raise ValidationError("This email is not associated with any user! ")

            user = Subscribe.objects.filter(email=data['email']).first()
            user.is_subscribed = True
            user.save()

            serializer.save()
            
            response = {"message": "Subscribed", "data": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    