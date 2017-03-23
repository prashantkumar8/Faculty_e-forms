from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone

from django.utils.encoding import python_2_unicode_compatible

class Person(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.CharField(max_length=200)
    # email = models.EmailField()
    # contact = models.IntegerField()
    # department = models.CharField(max_length=200)
    # date_of_joining = models.CharField(max_length=200)
    # blood_group = models.CharField(max_length=200)
    # residential_address = models.CharField(max_length=200)
    # pan_num = models.CharField(max_length=200)
    # account_num = models.IntegerField()
    # name_of_bank = models.CharField(max_length=200)
    # name_of_father = models.CharField(max_length=200)

    def __str__(self):
        return self.name