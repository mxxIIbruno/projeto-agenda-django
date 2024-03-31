from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact


def create(request):
    context = {
        ...: ...
    }
    return render(
        request=request,
        template_name='contact/create.html',
        context=context,
    )
