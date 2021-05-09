from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.site_header = "Приемная комиссия"
admin.site.site_title = "Приемная комиссия"
admin.site.index_title = "Приемная комиссия"

admin.site.unregister(Group)