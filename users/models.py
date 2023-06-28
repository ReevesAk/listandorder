from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

# UserManager handles the creation of superuser as well as manage creation of user accounts.
class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None, password2=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(
            username=username, 
            email=self.normalize_email(email),
            )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


# User describes the database model for each user.
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)    
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

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
