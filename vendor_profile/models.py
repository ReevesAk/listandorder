from django.db import models

from users.models import User

# Create your models here.
class Profile(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    address                 = models.CharField(max_length=100)
    phone_no                = models.CharField(max_length=50)
    business_CAC            = models.CharField(max_length=100)
    business_TIN            = models.CharField(max_length=100)
    nin                     = models.CharField(max_length=100)
    bvn                     = models.CharField(max_length=100)
    utility_bill            = models.CharField(max_length=100)
    Identification_no       = models.CharField(max_length=100)

    def __str__(self):
        return self.user
