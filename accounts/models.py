from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)

from orgs.models import Organization


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = email
    REQUIRED_FIELDS = []


class OrgAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    organization = models.ForeignKey(Organization, related_name='org_admins')

	
# class User(AbstractBaseUser):
# 	email 			= models.EmailField(max_length=255, unique=True)
#     STATUS_CHOICES  = (('merchants', 'Merchant'),('accounts', 'Accounts'))
#     user_type		= models.CharField(max_length=10, choices=STATUS_CHOICES, default='unsigned')
#     admin			= models.BooleanField(default=False)
#     active			= models.BooleanField(default=False)
#     date_created	= models.DateTimeField(auto_now_add=True)
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['user_type'] # Email & Password are required by default.

#     @property
#     def is_admin(self):
#         return self.admin
    
#     @property
#     def is_active():
#     	return self.active()

#     @property
#     def get_user_type(self):
#         return self.user_type


# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             email=self.normalize_email(email),
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password):
#         """
#         Creates and saves a superuser with the given email and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         user.staff = True
#         user.admin = True
#         user.save(using=self._db)
#         return user

    
    



