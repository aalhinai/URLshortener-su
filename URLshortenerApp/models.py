# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# table named ‘User_Urls’ in our database with the following field:
#
# short_id (it will store short URL id), (It is of max_length 8 and it is a primary key)
# short_url(it will store the  short_id with site_url
# httpurl (it will store URL), (It is of max_length 200)
# pub_date (It will store the date and time)
# count (It will store the number of times the URL is visited)

class Usr_Urls(models.Model):
      short_id = models.SlugField(max_length=8,primary_key=True, verbose_name='Short ID')
      short_url = models.URLField(max_length=60, verbose_name='Short URL')
      description = models.CharField(max_length=300, verbose_name='Description', default='No Description')
      httpurl = models.URLField(max_length=200, verbose_name='Orginal URL')
      pub_date = models.DateTimeField(auto_now=True, verbose_name='Created Data\Time')
      count = models.IntegerField(default=0, verbose_name='Visits')
      user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='User')
      

      class Meta:
        verbose_name = "Total URLs"
        verbose_name_plural = "Total URLs"

def __str__(self):
    return self.httpurl
