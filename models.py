from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_name = models.CharField(max_length=128)
    post_detail = models.TextField(max_length=10000, blank=True)

    def __str__(self):
        return self.post_name