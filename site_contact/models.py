from django.db import models

class Site(models.Model):
    site_name = models.CharField(max_length=100, unique=True)
    site_address = models.CharField(max_length=100, blank=True)
    site_contact = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.site_name

class Contact(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=13, blank=True)
    email = models.EmailField(blank=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.name