import json
from typing import Dict, Any

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse


def main_donate_page(request):
    context = {
        'make_donate_url': reverse('donations:make_donate'),
        'ask_donate_url': reverse('donations:ask_donate'),
        # 'main_url': reverse('donations:main')
    }
    return render(request, 'donate.html', context)


def make_donate(request):
    context = {
        'main_url': reverse('donations:main'),
        'thank_for_donate_url': reverse('donations:thank_for_donate')
    }
    with open('data.json', 'r') as file:
        cont = json.load(file)

    item = cont.append(
        {'name': request.POST['donation_item'], 'amount': request.POST['donation_amount']}
    )
    with open('data.json', 'w') as file:
        json.dump(cont, file)
    return render(request, 'thank_for_donate.html', context)


def list(request):
    context = {}
    with open('data.json', 'r') as file:
        context['file'] = json.load(file)
    return render(request, 'list.html', context)

def ask_donate(request):
    # context = {
    #     'main_url': reverse('donations:main'),
        # 'empty_cont_url': reverse('donations:empty_cont'),
        # 'full_url': reverse('donations:full_cont')
    # }
    item = None
    with open('data.json', 'r') as file:
        cont = json.load(file)

    if cont and request.method == 'POST':
        item = cont.pop()

        with open('data.json', 'w') as file:
            json.dump(cont, file)
    return render(request, 'ask_complete.html',  {'item': item, 'main_url': reverse('donations:main')})


def thank_for_donate(request):
    context = {
        'main_url': reverse('donations:main'),
        'thank_for_donate_url': reverse('donations:thank_for_donate')
    }
    return render(request, 'thank_for_donate.html', context)
