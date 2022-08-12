from re import T
from django.contrib import admin
from .models import History, Tradition, Art


# Register your models here.
admin.site.register(History)
admin.site.register(Tradition)
admin.site.register(Art)
