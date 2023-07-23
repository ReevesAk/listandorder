from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")

        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser):
    email = models.CharField(max_length=80, unique=True)
    username = models.CharField(max_length=45)
    date_of_birth = models.DateField(null=True)

    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username
    

class SendMail(models.Model):
    email = models.CharField(max_length=80, unique=True)
    subject = models.CharField(max_length=150)
    body = models.TextField()
    

class StockUpSchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    have_stock_up = models.BooleanField(default=False)
    stock_up_duration = models.DurationField(blank=True)


    def __str__(self):
        return self.user
    

    def stock_up(self):
        if self.stock_up_duration != None:
            self.have_stock_up == True
            return self.stock_up_duration
