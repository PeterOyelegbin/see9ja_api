from re import T
from django.contrib import admin
from .models import Tourism, Tradition, ArtsNCulture

# Register your models here.
admin.site.register(Tourism)
admin.site.register(Tradition)
admin.site.register(ArtsNCulture)
