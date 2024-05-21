from django.contrib.auth.models import AbstractUser
from django.db import models

class Kisi(AbstractUser):
    KisiMail = models.EmailField(blank=True,default='',unique=True)
    KisiPassword = models.CharField(max_length=20)