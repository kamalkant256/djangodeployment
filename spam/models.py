from django.db import models
from django.contrib.auth.models import  AbstractBaseUser

from Codeproject.manager import CustomUserManager

# Create your models here.

class UserMaster(AbstractBaseUser):
    name = models.CharField(max_length=250,null=True,blank=True)
    email = models.EmailField(max_length=250,null=True, blank=True,unique=True)
    mobile_number = models.CharField(max_length=16,null=True,blank=True,unique=True)
   

    objects = CustomUserManager()

    USERNAME_FIELD = 'mobile_number'
    REQUIRED_FIELDS = []
    
    class Meta:
        db_table = "user_master"
        indexes = [
            models.Index(fields=['email','mobile_number','id']),
        ]