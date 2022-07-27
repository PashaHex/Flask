from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

def main_donate_page(request):
    context = {
        'make_donate_url': reverse('donations:make_donate'),
        'ask_donate_url': ()
    }
    return render(request, 'donate.html', context)

def make_donate(request):
    return render(request, 'make_donate.html')
