
from django.db import models

class React(models.Model):
    food = models.CharField(max_length=30)
    ingredient = models.CharField(max_length=200)