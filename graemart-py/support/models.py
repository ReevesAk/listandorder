from django.db import models

# In_project imports.
from users.models import User

# Create your models here.

class ContactUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=155, null=True)
    phone_number = models.CharField(max_length=155, null=True)
    label = models.TextField()

    def __str__(self) -> str:
        return self.email


class Subscribe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=155, null=True)
    is_subscribed = models.BooleanField(default=False)
