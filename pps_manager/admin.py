from django.contrib import admin

# Register your models here.

from .models import BlacklistEntry, WhitelistEntry

admin.site.register(BlacklistEntry)
admin.site.register(WhitelistEntry)
