from django.db import models
import uuid
# Create your models here.

class User(models.Model):
    email = models.EmailField(blank=False)
    name = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=50, blank=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name
