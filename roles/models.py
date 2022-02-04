from django.db import models

class Role(models.Model):
    slug = models.CharField(
        max_length=100, 
        default='user', 
        primary_key=True
        )