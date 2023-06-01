from django.shortcuts import render, redirect
from eknowint.settings import LOGIN_URL
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin

#@login_required
#def loginpage(request):
#    return render(request, "login.html")


class Main(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "eknowint/main.html")
        else:
            return redirect(reverse_lazy("login") + "?next=" + request.path)
        
class LoginRequiredMixin(UserPassesTestMixin):
    LOGIN_URL = "login"
    redirect_field_name = "Main"

    def test_func(self):
        return self.request.user.is_authenticated
    

