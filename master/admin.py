from django.contrib import admin
from .models import (Company, Branch, Location, Vendor,  Category,  Brand, SoftwareType)

# Register your models here.
admin.site.register((Company, Branch, Location, Vendor, Category,  Brand, SoftwareType))