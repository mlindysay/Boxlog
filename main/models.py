from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone



class Box(models.Model):
    box_id = models.CharField(max_length=200)
    box_label = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.box_label
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Item(models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.item_name
 