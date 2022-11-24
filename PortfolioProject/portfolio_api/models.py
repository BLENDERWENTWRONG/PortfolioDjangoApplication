from django.db import models
from djongo import models

## models.py
from django.conf import settings

# Add the import for GridFSStorage
from djongo.storage import GridFSStorage

# Define your GrifFSStorage instance
grid_fs_storage = GridFSStorage(collection='myfiles', base_url=''.join(['myfiles/']))

# Create your models here.
from django.db import models
from django import forms


# Create your models here.
class Address(models.Model):
    country = models.CharField(max_length=100, null=False)
    region = models.CharField(max_length=100, null=False)
    street = models.CharField(max_length=100, null=False)
    postalCode = models.CharField(max_length=100, null=False)


class Accomplishments(models.Model):
    title = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=100, null=False)
    uploads = models.ImageField(upload_to='images')


class AH(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    uploads = models.ImageField(upload_to='images')


class DLC(models.Model):
    title = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=100, null=False)
    startDate = models.DateTimeField(auto_now=True, null=False)
    endDate = models.DateTimeField(auto_now=True, null=False)
    uploads = models.ImageField(upload_to='images', null=False)


class VCS(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, null=False)
    startDate = models.DateTimeField(auto_now=True, null=False)
    endDate = models.DateTimeField(auto_now=True, null=False)


class References(models.Model):
    contactInfo = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)
    jobTitle = models.CharField(max_length=100, null=False)


class User(models.Model):
    id = models.CharField(max_length=100, unique=True, primary_key=True)
    password = models.CharField(max_length=100)
    avatar = models.ImageField(width_field=128, height_field=128, upload_to='users', storage=grid_fs_storage)
    email = models.EmailField(max_length=100, unique=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    birthDate = models.DateField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE, default='')
    accomplishments = models.ForeignKey(Accomplishments, default='', on_delete=models.CASCADE)
    ah = models.ForeignKey(AH, default='', on_delete=models.CASCADE)
    dlc = models.ForeignKey(DLC, default='', on_delete=models.CASCADE)
    vcs = models.ForeignKey(VCS, default='', on_delete=models.CASCADE)
    references = models.ForeignKey(References, default='', on_delete=models.CASCADE)
