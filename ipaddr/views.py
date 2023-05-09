from django.shortcuts import render, redirect, get_object_or_404
from .models import IPAddress
from .forms import IPAddressForm

# Create your views here.

def ipaddr(request):
    ipaddresses = IPAddress.objects.all()
    return render(request, 'ipaddr/ipaddr.html', {'ipaddresses': ipaddresses})

def ipaddr_add(request):
    if request.method == 'POST':
        form = IPAddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ipaddr')
    else:
        form = IPAddressForm()
    return render(request, 'ipaddr/ipaddr_form.html', {'form': form})

def ipaddr_edit(request, pk):
    ipaddress = get_object_or_404(IPAddress, pk=pk)
    if request.method == 'POST':
        form = IPAddressForm(request.POST, instance=ipaddress)
        if form.is_valid():
            form.save()
            return redirect('ipaddr')
    else:
        form = IPAddressForm(instance=ipaddress)
    return render(request, 'ipaddr/ipaddr_form.html', {'form': form})

def ipaddr_delete(request, pk):
    ipaddress = get_object_or_404(IPAddress, pk=pk)
    ipaddress.delete()
    return redirect('ipaddr')
