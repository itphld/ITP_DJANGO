from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,email,mobile,username,password):
        if not username:
            raise ValueError("Username  can't be blank")
        if not email:
            raise ValueError("Email Field Can't Be Blank")
        if not mobile:
            raise ValueError("Moble is Mandatory")
        user=self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            username=username,
            mobile=mobile
        )
        user.set_password(password)
        user.save()
        return user
        #user.save(using=self._db)
    def create_superuser(self, first_name, last_name, email, mobile, username, password):

        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            mobile=mobile,
            username=username,
            password=password,
            )

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user

class Account(AbstractBaseUser,PermissionsMixin):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    mobile=models.CharField(max_length=12)
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)
    #required Field

    is_active=models.BooleanField(default=True)

    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name','username','mobile']
    objects=MyAccountManager()

    def __str__(self):
        return self.email
    def has_perm(self,perm,object=None):
        return self.is_superuser
    def has_module_perm(self,app_label):
        return True
