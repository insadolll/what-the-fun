from django import forms
from .models import Site, Contact

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['site_name', 'site_address', 'site_contact']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'position', 'phone', 'email', 'note']