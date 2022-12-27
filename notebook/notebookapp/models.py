from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Note(models.Model):
	name = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
