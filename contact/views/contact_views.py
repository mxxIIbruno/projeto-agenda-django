from django.shortcuts import render, get_object_or_404
from contact.models import Contact


def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]

    context = {
        'contacts': contacts,
    }

    return render(
        request=request,
        template_name='contact/index.html',
        context=context,
    )


def contact(request, contact_id):
    # single_contact = Contact.objects.get(pk=contact_id)
    single_contact = get_object_or_404(
        Contact.objects,
        pk=contact_id,
        show=True,
    )

    context = {
        'contact': single_contact,
    }

    return render(
        request=request,
        template_name='contact/contact.html',
        context=context,
    )
