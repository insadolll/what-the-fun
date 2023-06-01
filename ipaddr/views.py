from django.shortcuts import render, redirect, get_object_or_404
from .models import IPAddress
from .forms import IPAddressForm
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def ipaddr(request):
    ipaddresses = IPAddress.objects.all().order_by('ip_address')
    return render(request, 'ipaddr/ipaddr.html', {'ipaddresses': ipaddresses})

def ipaddr_add(request):
    if request.method == 'POST':
        form = IPAddressForm(request.POST)
        if form.is_valid():
            ip = form.save(commit=False)
            ip.ip_id = form.cleaned_data['ip_id']
            ip.ip_pw = form.cleaned_data['ip_pw']
            ip.save()
            return redirect('ipaddr')
    else:
        form = IPAddressForm()
    return render(request, 'ipaddr/ipaddr_form.html', {'form': form})

def ipaddr_edit(request, pk):
    ipaddress = get_object_or_404(IPAddress, pk=pk)
    if request.method == 'POST':
        form = IPAddressForm(request.POST, instance=ipaddress)
        if form.is_valid():
            ip = form.save(commit=False)
            ip.ip_id = form.cleaned_data['ip_id']
            ip.ip_pw = form.cleaned_data['ip_pw']
            ip.save()
            return redirect('ipaddr')
    else:
        form = IPAddressForm(instance=ipaddress)
    return render(request, 'ipaddr/ipaddr_form.html', {'form': form})

def ipaddr_delete(request, pk):
    ipaddress = get_object_or_404(IPAddress, pk=pk)
    ipaddress.delete()
    return redirect('ipaddr')
