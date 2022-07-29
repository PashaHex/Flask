import json

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse


def main_donate_page(request):
    context = {
        'make_donate_url': reverse('donations:make_donate'),
        'ask_donate_url': reverse('donations:ask_donate'),
        'main_url': reverse('donations:main')
    }
    return render(request, 'donate.html', context)


def make_donate(request):
    context = {
        'main_url': reverse('donations:main'),
        'make_donate_url': reverse('donations:make_donate')
    }
    with open('data.json', 'r') as f:
        data = f.read()
        if data:
            cont = json.load(data)
        else:
            cont = []

    row_dict = {'name': {request.POST['donation_item']}, 'amount': {request.POST['donation_amount']}}
    cont.append(row_dict)

    with open('data.json', 'w') as f:
        json.dump(cont, f)

    return render(request, 'make_donate.html', context)


def ask_donate(request):
    # item = None
    # with open('data.json', 'r') as f:
    #     cont = json.load(f)
    #
    # if cont:
    #     item = cont.pop()
    #
    #     with open('data.json', 'w') as f:
    #         json.dump(cont, f)
    #
    # return render(request, 'empty_cont.html', {'item': item})

    context = {
        'main_url': reverse('donations:main')
    }

    with open('data.json', 'r') as f:
        data = f.read()
        if data:
            cont = json.load(data)
        else:
            cont = []

    if not cont:
        return render(request, 'empty_cont.html', context)

    item = cont.pop()
    with open('data.json', 'w') as f:
        json.dump(cont, f)

    return render(request, 'full_cont.html', item=item)
