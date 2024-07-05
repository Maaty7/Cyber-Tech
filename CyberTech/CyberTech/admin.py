from django.contrib import admin
from .models import Tecnologia, Hardware, Periferico, Electrodomestico

# Register your models here.

admin.site.register(Tecnologia)
admin.site.register(Hardware)
admin.site.register(Periferico)
admin.site.register(Electrodomestico)
