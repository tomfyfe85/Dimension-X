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

    # def __eq__(self, other):
    #     return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"DeeX({self.full_name}, {self.user_name}, {self.password}, {self.email}, {self.deeX}, {self.slug}, {self.date_time})"
