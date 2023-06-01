from django import forms
from .models import IPAddress

class IPAddressForm(forms.ModelForm):
    class Meta:
        model = IPAddress
        fields = ('status', 'ip_address', 'netmask', 'gateway', 'hostname', 'os', 'ip_id', 'ip_pw', 'note')