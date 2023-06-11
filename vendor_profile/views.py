from django.shortcuts import get_object_or_404

# Third party imports.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

# In_project imports
from . serializers import ProfileSerializer
from .models import Profile

# Create your views here.
class CreateProfile(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class RetrieveProfile(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class DeleteProfile(generics.DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UpdateProfile(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ListAllProfiles(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    