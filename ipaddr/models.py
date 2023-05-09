from django.db import models

# Create your models here.
class IPAddress(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )

    ip_address = models.CharField(max_length=15, unique=True)
    netmask = models.CharField(max_length=15)
    gateway = models.CharField(max_length=15)
    hostname = models.CharField(max_length=50, blank=True)
    os = models.CharField(max_length=50)
    note = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.ip_address