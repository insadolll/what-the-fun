from django.shortcuts import render
from .models import Contact

def ek_contact_list(request):
    if request.user.is_authenticated:  # 사용자가 인증되어 있는지 확인
        user = request.user  # 현재 로그인된 사용자
        contacts = Contact.objects.filter(user=user)
    else:
        contacts = []

    return render(request, 'ek_contact/ek_contact_list.html', {'contacts': contacts})

