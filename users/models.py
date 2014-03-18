from django.db import models
from django.contrib.auth.models import User
  
class UserProfile(models.Model):
    # self field is required.
    user = models.OneToOneField(User)