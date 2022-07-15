from django.contrib import admin

from .models import Request_donate

class DonateAdmin(admin.ModelAdmin):
    fields = ['ask', 'make donate']

admin.site.register(Request_donate, DonateAdmin)