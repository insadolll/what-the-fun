from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
# Create your models here.
