from django import forms
from .models import (Company, Branch, Location, Vendor,  Category,  Brand, SoftwareType)
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

# COMPANY MASTER FORM
class CompanyForm(forms.ModelForm):
    contact = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial="IN"))
    
    class Meta:
        model = Company
        fields = ['company_name','address','contact','email','website']
        

# BRANCH MASTER FORM


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['company', 'branch_name','address']

# EMPLOYEE LOCATION MASTER FORM


class Employee_LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['location_type','branch', 'location']

# VENDOR FORM


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'


#ASSET LOCATION FORM
# class Asset_LocationForm(forms.ModelForm):
#     class Meta:
#         model = Location
#         fields = ['branch', 'location']

#CATEGORY FORM
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['asset_type', 'category']

#SUBCATEGORY FORM
# class SubCategoryForm(forms.ModelForm):
#     class Meta:
#         model =Category
#         fields = ['category', 'name']

#BRAND FORM
class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']

#SOFTWARE TYPE FORM
class SoftwareTypeForm(forms.ModelForm):
    class Meta:
        model = SoftwareType
        fields = ['type']