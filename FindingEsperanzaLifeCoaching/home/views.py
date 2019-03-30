from django.shortcuts import render

from wagtail.core.models import Page


def landing(result):
    return render(request, 'home/landing.html', context={})
