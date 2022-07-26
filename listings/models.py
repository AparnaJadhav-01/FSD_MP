from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, auth
from apts.views import fav_post, favorites
from django.shortcuts import render
from django.urls import reverse

# Create your models here.
class Listing(models.Model):
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=20)
  description = models.TextField(blank=True)
  price = models.IntegerField()
  bedrooms = models.IntegerField()
  park_lot = models.BooleanField(default=True)
  sqft = models.IntegerField()
  photo_main = models.ImageField(null=True,blank=True)
  photo_1 = models.ImageField( null=True,blank=True)
  photo_2 = models.ImageField( null=True,blank=True)
  photo_3 = models.ImageField( null=True,blank=True)
  photo_4 = models.ImageField( null=True,blank=True)
  photo_5 = models.ImageField( null=True,blank=True)
  photo_6 = models.ImageField( null=True,blank=True)
  fav =models.ManyToManyField(User,related_name='fav',blank=True)
  is_furnished = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  ownerName = models.CharField(max_length=200,default="Unknown")
  ownerPh = models.CharField(max_length=200,default="Unknown")
  ownerInfo = models.CharField(max_length=200,default="Unknown")
  
  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('apts:favorites', args=[str(self.id)])