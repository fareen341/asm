import email
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
# from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
# from gst_field.modelfields import GSTField

# Create your models here.
# COMPANY


class Company(models.Model):
    company_name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    contact =PhoneNumberField(blank=True, help_text='Contact phone number')
    email = models.EmailField()
    website = models.CharField(max_length=50,null=True,blank=True)
    # gst = GSTField()
    def __str__(self):
        return self.company_name

# BRANCH


class Branch(models.Model):
    company = models.ForeignKey("Company", on_delete=models.PROTECT)
    branch_name = models.CharField(max_length=20)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.branch_name


#LOCATION


class Location(models.Model):
    location_type=models.CharField(choices=(('Employee Location','Employee Location'),('Asset Location','Asset Location')),max_length=50)
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location

# VENDOR


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=50)
    # vendor_code = models.CharField(max_length=50)
    vendor_contact = PhoneNumberField(blank=True, help_text='Contact phone number')
    vendor_email = models.EmailField()
    vendor_website = models.CharField(max_length=50,null=True,blank=True)
    vendor_address = models.CharField(max_length=100)
    # vendor_gst = GSTField()
    vendor_contact_person =models.CharField(max_length=50)
    vendor_contact_person_contact = PhoneNumberField(blank=True, help_text='Contact phone number')
    

    def __str__(self):
        return self.vendor_name
    
    def vendor_code(self):
        
        if len(str(self.pk))== 1:
            vendor_code="ZITV000" + str(self.pk)
            return vendor_code
        elif len(str(self.pk))==2:
            vendor_code="ZITV00" + str(self.pk)
            return vendor_code
        elif len(str(self.pk))== 3:
            vendor_code="ZITV0" + str(self.pk)
            return vendor_code
    
    

# ASSET LOCATION


# class Asset_Location(models.Model):
#     branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
#     location = models.CharField(max_length=50)

#     def __str__(self):
#         return self.location

# CATEGORY


class Category(models.Model):
    asset_type=models.CharField(choices= (('IT Assets', 'IT Assets'),('Non IT Assets', 'Non IT Assets')),max_length=50)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

# SUBCATEGORY


# class SubCategory(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.PROTECT)
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

# BRAND


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# SOFTWARE TYPE


class SoftwareType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type