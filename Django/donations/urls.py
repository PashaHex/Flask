from django.urls import path, re_path

from . import views

app_name = 'donations'

urlpatterns = [
    path('', views.main_donate_page, name='main'),
    path('make_donate', views.make_donate, name='make_donate'),
    path('ask_donate', views.ask_donate, name='ask_donate'),
    path('list', views.list, name='list'),
    path('thank_for_donate', views.thank_for_donate, name='thank_for_donate'),
]
