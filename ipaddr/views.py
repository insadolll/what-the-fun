from django.shortcuts import render

# Create your views here.
def ipaddr(request):
    return render(request,'ipaddr/ipaddr.html')