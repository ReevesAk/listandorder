from django.db import models

from users.models import User

# Create your models here.
class Checkout(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name              = models.CharField(max_length=50)
    last_name               = models.CharField(max_length=50)
    apartment               = models.CharField(max_length=100)
    postal_address          = models.CharField(max_length=100)
    zipcode                 = models.CharField(max_length=100, blank=True)
    city                    = models.CharField(max_length=100, blank=True)
    state                   = models.CharField(max_length=100, blank=True)
    country                 = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.user
