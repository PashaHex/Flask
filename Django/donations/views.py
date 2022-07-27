from django.shortcuts import render
from django.http import HttpResponse

def main_donate_page(request):
    context = {
        'make_donate-url': (),
        'ask_donate_url': ()
    }
    return render(request, 'donate.html')

def make_donate(request):
    return render(request, 'make_donate.html')
