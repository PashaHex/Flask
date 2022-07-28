import json

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

def main_donate_page(request):
    context = {
        'make_donate_url': reverse('donations:make_donate'),
        # 'ask_donate_url': ()
    }
    return render(request, 'donate.html', context)

def make_donate(request):
    with open('data.json', 'r') as f:
        cont = json.load(f)

    row_dict = {'name': request.POST['donation_item'], 'amount': request.POST['donation_amount']}
    cont.append(row_dict)

    with open('data.json', 'w') as f:
        json.dump(cont, f)

    return render(request, 'thank_for_donate.html')
