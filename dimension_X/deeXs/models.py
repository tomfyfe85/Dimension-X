from django.db import models


# email, password, name and a username
# Create your models here.
class Deex(models.Model):
  full_name = models.CharField(max_length=50)