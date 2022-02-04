from django.db import models
from django.contrib.postgres.fields import ArrayField

from users.models import User

class Target(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    months = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    completed = models.BooleanField(default=False)
    price = models.CharField(max_length=255)
    pros = ArrayField(models.TextField(), null=True)
    minuses = ArrayField(models.TextField(), null=True)
    images = ArrayField(models.TextField(), null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = [
        'id', 
        'user_id', 
        'months', 
        'title', 
        'completed',
        'price', 
        'created_at'
    ]