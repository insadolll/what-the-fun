from sqlite3 import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from .models import Site, Contact
from .forms import SiteForm, ContactForm

def site_list(request):
    sites = Site.objects.all()
    return render(request, 'site_contact/site_list.html', {'sites': sites})

def site_detail(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    return render(request, 'site_contact/site_detail.html', {'site': site})

def site_create(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('site_list')
            except IntegrityError:
                form.add_error('site_name', '중복된 이름')
    else:
        form = SiteForm()
    return render(request, 'site_contact/site_form.html', {'form': form})

def site_update(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('site_detail', site_id=site_id)
    else:
        form = SiteForm(instance=site)
    return render(request, 'site_contact/site_form.html', {'form': form})

def site_delete(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    if request.method == 'POST':
        site.delete()
        return redirect('site_list')
    return render(request, 'site_contact/site_confirm_delete.html', {'site': site})

def contact_create(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.site = site
            contact.save()
            return redirect('site_detail', site_id=site_id)
    else:
        form = ContactForm()
    return render(request, 'site_contact/contact_form.html', {'form': form, 'site': site})

def contact_update(request, site_id, contact_id):
    site = get_object_or_404(Site, pk=site_id)
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('site_detail', site_id=site_id)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'site_contact/contact_form.html', {'form': form, 'site': site})

def contact_delete(request, site_id, contact_id):
    site = get_object_or_404(Site, pk=site_id)
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('site_detail', site_id=site_id)
    return render(request, 'site_contact/contact_confirm_delete.html', {'contact': contact, 'site': site})

