from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactModelForm
from .models import Contact


def product_create_view(request):
    form = ContactModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ContactModelForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)
