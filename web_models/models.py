# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Test(models.Model):

    UserName = models.CharField(max_length=255)

    PassWord = models.CharField(max_length=255)