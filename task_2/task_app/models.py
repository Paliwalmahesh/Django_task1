from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    ph_no = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=10)

    def _str_(self):
        return self.l_name

# Create your models here.
