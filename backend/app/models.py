
from django.db import models
# define class
class React(models.Model):
    food = models.CharField(max_length=30)
    ingredient = models.CharField(max_length=200)