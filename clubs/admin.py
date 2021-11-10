from django.contrib import admin

from .models import Group, Groupnotices, Groupresults
admin.site.register(Group)
admin.site.register(Groupnotices)
admin.site.register(Groupresults)
