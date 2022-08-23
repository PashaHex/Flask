from django.contrib import admin

from .models import Request_donate, Office

class DonateAdmin(admin.ModelAdmin):
    exclude = ['id']
    # fields = ['ask', 'make donate']

admin.site.register(Request_donate, DonateAdmin)

class OfficeAdmin(admin.ModelAdmin):
    exclude = ['id']
    # fields = ['name', 'capacity', 'occupied']

admin.site.register(Office, OfficeAdmin)