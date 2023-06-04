from django.urls import path
from . views import *

urlpatterns = [
    path("create_profile/", CreateProfile.as_view(), name="create_profile"),
    path("all_profiles/", ListAllProfiles.as_view(), name = "all_profiles"),
    path("delete_profile/<int:id>/", DeleteProfile.as_view(), name="delete_profile"),
    path("update_profile/<int:id>/", UpdateProfile.as_view(), name="update_profile"),
    path("get_profile/<int:id>/", RetrieveProfile.as_view(), name="get_profile")
]