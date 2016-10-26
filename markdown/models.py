from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Document model
class Document(models.Model):
  # title
  title = models.CharField(max_length=100)
  # content
  content = models.TextField()
  # create time
  create_date = models.DateTimeField(auto_now=True)
  # creator/owner
  creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
  # current editor
  editor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='editor')
  # last saved time
  last_saved_time = models.DateTimeField(auto_created=True)
  # shared user
  shared_user = models.ManyToManyField(User, related_name='shared_users', blank=True)
  # if this doc has been deleted
  is_delete = models.CharField(max_length=1, default='0')

# Create your models here.
class UserExtend(models.Model):
  # user object
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  # age
  age = models.CharField(max_length=5, null=True, default='')
  # self biography
  biography = models.CharField(max_length=300, null=True, default='')
  # user avatar
  avatar = models.ImageField(upload_to='user-avatars', default='user-avatars/default_avatar.png')
  # activated token
  token = models.CharField(max_length=50, null=True)
  # shared document
  shared_document = models.ManyToManyField(Document, related_name='shared_docs', blank=True)
  # reverse data 1
  reserve1 = models.CharField(max_length=1, null=True)
  # reverse data 2
  reserve2 = models.CharField(max_length=50, null=True)

