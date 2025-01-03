from django.db import models
from django.contrib.auth.models import User
from .utils import user_directory_path


class Location(models.Model):
    country=models.CharField(max_length=50,blank=True)
    district=models.CharField(max_length=50,blank=True)
    address_line1=models.CharField(max_length=50,blank=True)
    address_line2=models.CharField(max_length=50,blank=True)
    def __str__(self):
        return f'LOCATION {self.id}'

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    photo=models.ImageField(null=True,upload_to=user_directory_path)
    bio=models.CharField(max_length=140,blank=True)
    phone_number=models.CharField(max_length=12,blank=True)
    email=models.EmailField( max_length=254,blank=True)
    location=models.OneToOneField(Location,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.user.username}\'s profile'