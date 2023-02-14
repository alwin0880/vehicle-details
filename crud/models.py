from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser,UserManager
from django.contrib.auth.models import PermissionsMixin
# Create your models here.


class User(AbstractBaseUser,PermissionsMixin):
    ROLE_CHOICES = (
        ('Super Admin', 'Super Admin'),
        ('Admin', 'Admin'),
        ('User', 'User'),
    )
    email = models.EmailField(max_length=255)
    username = models.CharField(max_length=255,unique=True)
    role = models.CharField(choices=ROLE_CHOICES,max_length=15,default="User")
    is_staff=models.BooleanField(default=False)
    

    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    
    def can_create(self):
        return self.role == 'Super Admin'
    
    def can_read(self):
        return self.role in ["User",'Admin','Super Admin']
    
    def can_update(self):
        return self.role in ['Super Admin', 'Admin']
    
    def can_delete(self):
        return self.role == 'Super Admin'




class Vehicle(models.Model):

    vehicle_choices=(
        ("Two","Two Wheeler"),
        ("Three","Three Wheeler"),
        ("Four","Four Wheeler"),
        )
    vehicle_number=models.CharField(max_length=10,validators=[RegexValidator(r'^[0-9a-zA-Z]*$',message="Enter a valid Number",)])
    vehicle_type=models.CharField(max_length=15,choices=vehicle_choices,default="Two")
    vehicle_model=models.CharField(max_length=50)
    vehicle_description=models.CharField(max_length=100)
   

    def __str__(self):
        return self.vehicle_model