from django.contrib import admin
from .models import Laptops

@admin.register(Laptops)
class LaptopsAdmin(admin.ModelAdmin):
    pass