from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .forms import ContactForm
from .models import Contacts


def index(request):
    contact_list = Contacts.objects.order_by('-created_date')[:4]
    template = loader.get_template('contacts/index.html')
    context = {
        'contact_list': contact_list,
    }
    return HttpResponse(template.render(context, request))


def create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_list = Contacts.objects.order_by('-created_date')[:4]
            template = loader.get_template('contacts/index.html')
            context = {
                'contact_list': contact_list,
            }
            Contacts.save(Contacts(
                first_name=form.data.get('first_name'),
                last_name=form.data.get('last_name'),
                phone_number=form.data.get('phone_number'),
                email=form.data.get('email')
            ))
            return HttpResponse(template.render(context, request))
    else:
        form = ContactForm()
    return render(request, 'contacts/create.html', {'form': form})
