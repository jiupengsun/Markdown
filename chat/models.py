from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
'''
websocket test
'''
class Room(models.Model):
  name = models.TextField()
  label = models.SlugField(unique=True)

class Message(models.Model):
  room = models.ForeignKey(Room, related_name='messages')
  handle = models.TextField()
  message = models.TextField()
  timestamp = models.DateTimeField(default=timezone.now, db_index=True)
'''
websocket test
'''
