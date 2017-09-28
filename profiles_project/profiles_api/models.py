from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractBaseUser ## base of django built-in user modal
from django.contrib.auth.models import PermissionsMixin ### sets permission to users
from django.contrib.auth.models import BaseUserManager  ### default user manager of django


class UserProfileManager(BaseUserManager):
    """ helps django work with our custom user model """

    def create_user(self, email, name, password):
        """ creates a new user profile objec """

        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)
        user  = self.model(email=email)
        user.set_password(password)##encripts the password into HASH
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """ creates a new superuser just created """

        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff     = True

        user.save(using=self._db)
        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ Represents the userprofile inside our system """

    email           = models.EmailField(max_length=255 , unique=True)
    name            = models.CharField(max_length=255)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)

    objects         = UserProfileManager()   # object manager class to help manage the user profile like createing admin user or creating normal user

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['name']

    #helper function

    def get_full_name(self):
        """ User to get a user full name"""
        return self.name #self is base and it hits name filed

    def get_short_name(self):
        """ use to get a user short name """
        return self.name

    def __str__(self):
        """ django uses this when it requires to convert OBJECT into a STRING """
        return self.email
