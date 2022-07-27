from django.urls import path, re_path

from . import views

app_name = 'donations'

urlpatterns = [
    path('', views.main_donate_page, name='main'),
    path('make_donate', views.make_donate, name='make_donate'),
]