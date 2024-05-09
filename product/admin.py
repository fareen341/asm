from django.contrib import admin
from .models import (Software,Hardware,Nonitasset)

# Register your models here.
admin.site.register((Software,Hardware,Nonitasset))