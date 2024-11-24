from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError("email should be there")
        if not username:
            raise ValueError("username should be there")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        # set password
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50)

    # req field

    date_joined = models.DateTimeField(auto_now_add=True)
    last_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_prem(self, prem, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
