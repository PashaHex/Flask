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
    with open('data.json', 'r') as f:
        cont = json.load(f)

    item = cont.append(
        {'name': request.POST['donation_item'], 'amount': request.POST['donation_amount']}
    )
    with open('data.json', 'w') as f:
        json.dump(cont, f)
    return render(request, 'thank_for_donate.html', context)


def list(request):
    # context{}
    with open ('data.json', 'r') as f:
        context['f'] = json.load(f)
    return render(request, 'list.html')

def ask_donate(request):
    context = {
        'main_url': reverse('donations:main'),
        'empty_cont_url': reverse('donations:empty_cont'),
        'full_url': reverse('donations:full_cont')
    }
    # item = None
    with open('data.json', 'r') as f:
        cont = json.load(f)

    if not cont or request.method != 'POST':
        return render(request, 'empty_cont.html', context)  # , {'item': item})
        # return HttpResponse(  f'''
        #         <html>
        #           <body>
        #             <h3> Ничего нет для вас </h3>
        #             <a href='/'> Back to main </a>
        #           </body>
        #         </html>
        #         '''        )

    item = cont.pop()
    with open('data.json', 'w') as f:
        json.dump(cont, f)
    return render(request, 'full_cont.html', context) #, item=item)
    # return HttpResponse(        f'''
    #     <html>
    #       <body>
    #         <h3> Вот вам, возьмите </h3>
    #         {item['name']} {item['amount']}
    #         <a href='/'> Back to main </a>
    #       </body>
    #     </html>
    #     '''    )

    # if cont:
    #     item = cont.pop()
    #     with open('data.json', 'w') as f:
    #         json.dump(cont, f)
    # return render(request, 'empty_cont.html') #, {'item': item})

    # with open('data.json', 'r') as f:
    #     data = f.read()
    #     if data:
    #         cont = json.load(data)
    #     else:
    #         cont = []
    #
    # if not cont:
    #     return render(request, 'empty_cont.html', context)
    #
    # item = cont.pop()
    # with open('data.json', 'w') as f:
    #     json.dump(cont, f)
    #
    # return render(request, 'full_cont.html', item=item)

def thank_for_donate(request):
    context = {
        'main_url': reverse('donations:main'),
        'thank_for_donate_url': reverse('donations:thank_for_donate')
    }
    return render(request, 'thank_for_donate.html', context)
