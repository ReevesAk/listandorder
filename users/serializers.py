import re

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError

from .models import User, StockUpSchedule, SendMail

class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=45)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["email", "username", "password"]

    def validate(self, attrs):

        email = attrs.get('email', '')

        email_exists = User.objects.filter(email=attrs["email"]).exists()

        if email_exists:
            raise ValidationError("Email has already been used")
        
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email) == None:
            return serializers.ValidationError(
                'email: email is not valid'
            )

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)

        user.set_password(password)
        
        user.save()

        Token.objects.create(user=user)

        return user

    
    
# LoginSerializer is a  serializer class for login credentials. 
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    
    class Meta:
        model = User
        fields = ['email','password']


class SendMailSerializer(serializers.ModelSerializer):

    class Meta:
        model = SendMail
        fiels = ['email', 'subject', 'body']

    def validate(self, attrs):

        email = attrs.get('email', '')

        email_exists = User.objects.filter(email=attrs["email"]).exists()

        if not email_exists:
            raise ValidationError("Email is  not registered with us.")
        
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email) == None:
            return serializers.ValidationError(
                'email: email is not valid'
            )

        return super().validate(attrs)

        
# StockUpScheduleSerializer is a serializer for schedule 
# for product stockup.
class StockUpScheduleSerializer(serializers.ModelSerializer):

     class Meta:
        model = StockUpSchedule
        fields = ['id', 'have_stock_up', 'stock_up_duration']
