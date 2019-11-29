from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime


# Create your models here.


class Clothing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
    Brand = models.ForeignKey('Brand', null=True, blank=True, on_delete=models.CASCADE)
    itemname = models.CharField(max_length=255)
    desc = models.TextField(max_length=800)
    keywords = models.TextField(max_length=255)
    price = models.IntegerField()
    color = models.CharField(max_length=255)
    image = models.FileField(upload_to='images')
    image2 = models.FileField(upload_to='images', null=True)
    image3 = models.FileField(upload_to='images', null=True)
    itemid = models.CharField(max_length=120)

    def __str__(self):
        return self.itemname

class Promo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=800)
    image = models.FileField(upload_to='images')

    def __str__(self):
        return self.name


# Category for clothing
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


# Brand class
class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    desc = models.TextField(max_length=800)

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "Brand"

    def __str__(self):
        return self.name
