from django.db import models


# email, password, name and a username
# Create your models here.
class DeeX(models.Model):
    full_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    deeX = models.TextField(max_length=140)
    slug = models.SlugField()
    date_time = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.full_name
 