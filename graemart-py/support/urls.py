from django.urls import path

from .views import ContactGraemart, Subscribe

urlpatterns = [
    path('contact-us', ContactGraemart.as_view(), name='contact_us'),
    path('subscribe/', Subscribe.as_view(), name='subscribe'),
]
