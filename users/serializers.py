import re

from rest_framework import serializers

from .models import User, StockUpSchedule

class SignUpSerializer(serializers.ModelSerializer):
    """ Serailizers for our User first time registration """

    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    
    password2 = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email','password', 'password2']


    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        password2 = attrs.get('password2', '')
        
        if password != password2:
            return serializers.ValidationError(
                'password: Passwords do not match'
            )

        if email is None:
            return serializers.ValidationError(
                'email: email field can not be empty'
            )
        
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email) == None:
            return serializers.ValidationError(
                'email: email is not valid'
            )
        
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)     
    
    
# LoginSerializer is a  serializer class for login credentials. 
class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    
    class Meta:
        model = User
        fields = ['email','password']


# StockUpScheduleSerializer is a serializer for schedule 
# for product stockup.
class StockUpScheduleSerializer(serializers.ModelSerializer):

     class Meta:
        model = StockUpSchedule
        fields = ['id', 'have_stock_up', 'stock_up_duration']
