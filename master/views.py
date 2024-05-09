from django.shortcuts import get_object_or_404, render,reverse, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib import messages
from .models import (Company, Branch,  Vendor,
                     Location, Category,  Brand, SoftwareType)
from .forms import (CompanyForm, BranchForm, Employee_LocationForm, VendorForm,
                    CategoryForm,  BrandForm, SoftwareTypeForm)
#  Asset_LocationForm,SubCategoryForm,


# COMPANY MASTER CREATE
@method_decorator(login_required, name='dispatch')
class CompanyCreateView(generic.CreateView):
    template_name = 'master/company/company_create.html'
    form_class = CompanyForm

    def get_success_url(self):
        messages.success(self.request, 'Company Created Sucessfully')
        return reverse("CompanyList")


# COMPANY MASTER LIST
@method_decorator(login_required, name='dispatch')
class CompanyListView(generic.ListView):
    template_name = "master/company/company_list.html"
    queryset = Company.objects.all()
    context_object_name = "company"
    
# COMPANY MASTER Update

@method_decorator(login_required, name='dispatch')
class CompanyUpdateView(generic.UpdateView):
    template_name = "master/company/company_create.html"
    form_class=CompanyForm
    queryset = Company.objects.all()
    context_object_name = "company"
    
    def get_success_url(self):
        return reverse("CompanyList")


# COMPANY BRANCH CREATE
@method_decorator(login_required, name='dispatch')
class BranchCreateView(generic.CreateView):
    template_name = 'master/branch/branch_create.html'
    form_class = BranchForm

    def get_success_url(self):
        messages.success(self.request, 'Branch Created Sucessfully')
        return reverse("BranchList")
    
# Company Branch Update
@method_decorator(login_required, name='dispatch')
class BranchUpdateView(generic.UpdateView):
    template_name = "master/branch/branch_create.html"
    form_class=BranchForm
    queryset = Branch.objects.all()
    context_object_name = "branch"
    
    def get_success_url(self):
        return reverse("BranchList")


# COMPANY BRANCH LIST
@method_decorator(login_required, name='dispatch')
class BranchListView(generic.ListView):
    template_name = "master/branch/branch_list.html"
    queryset = Branch.objects.all()
    context_object_name = "branch"


# COMPANY EMPLOYEE LOCATION CREATE
@method_decorator(login_required, name='dispatch')
class EmployeeLocationCreateView(generic.CreateView):
    template_name = 'master/location/employee_location_create.html'
    form_class = Employee_LocationForm

    def get_success_url(self):
        messages.success(self.request, 'Employee Location Created Sucessfully')
        return reverse("EmployeeLocationList")


# COMPANY EMPLOYEE LOCATION LIST
@method_decorator(login_required, name='dispatch')
class EmployeeLocationListView(generic.ListView):
    template_name = "master/location/employee_location_list.html"
    queryset = Location.objects.all()
    context_object_name = "e_location"
    
# COMPANY EMPLOYEE LOCATION UPDATE
@method_decorator(login_required, name='dispatch')
class ElocationUpdateView(generic.UpdateView):
    template_name = "master/location/employee_location_create.html"
    form_class=Employee_LocationForm
    queryset = Location.objects.all().order_by("branch")
    context_object_name = "e_location"
    
    def get_success_url(self):
        return reverse("EmployeeLocationList")


# VENDOR CREATE
@method_decorator(login_required, name='dispatch')
class VendorCreateView(generic.CreateView):
    template_name = 'master/vendor/vendor_create.html'
    form_class = VendorForm

    def get_success_url(self):
        messages.success(self.request, 'Vendor Created Sucessfully')
        return reverse("VendorList")


# VENDOR LIST
@method_decorator(login_required, name='dispatch')
class VendorListView(generic.ListView):
    template_name = "master/vendor/vendor_list.html"
    queryset = Vendor.objects.all()
    context_object_name = "vendor"

# VENDOR Update
@method_decorator(login_required, name='dispatch')
class VendorUpdateView(generic.UpdateView):
    template_name = "master/vendor/vendor_update.html"
    form_class=VendorForm
    queryset = Vendor.objects.all()
    context_object_name = "vendor"
    
    def get_success_url(self):
        return reverse("VendorList")


# COMPANY ASSET LOCATION CREATE
# @method_decorator(login_required, name='dispatch')
# class AssetLocationCreateView(generic.CreateView):
#     template_name = 'master/location/asset_location_create.html'
#     form_class = Asset_LocationForm

#     def get_success_url(self):
#         messages.success(self.request, 'Branch Created Sucessfully')
#         return reverse("AssetLocationList")


# # COMPANY ASSET LOCATION LIST
# @method_decorator(login_required, name='dispatch')
# class AssetLocationListView(generic.ListView):
#     template_name = "master/location/asset_location_list.html"
#     queryset = Asset_Location.objects.all()
#     context_object_name = "a_location"
    
# COMPANY ASSET LOCATION UPDATE
# @method_decorator(login_required, name='dispatch')
# class AssetLocationUpdateView(generic.UpdateView):
#     template_name = "master/location/asset_location_create.html"
#     form_class=Asset_LocationForm
#     queryset = Asset_Location.objects.all()
#     context_object_name = "a_location"
    
#     def get_success_url(self):
#         return reverse("AssetLocationList")


# PRODUCT CATEGORY CREATE
@method_decorator(login_required, name='dispatch')
class CategoryCreateView(generic.CreateView):
    template_name = 'master/category/category_create.html'
    form_class = CategoryForm

    def get_success_url(self):
        messages.success(self.request, 'Category Created Sucessfully')
        return reverse("CategoryList")


# PRODUCT CATEGORY LIST
@method_decorator(login_required, name='dispatch')
class CategoryListView(generic.ListView):
    template_name = "master/category/category_list.html"
    queryset = Category.objects.all()
    context_object_name = "category"
    
# PRODUCT CATEGORY UPDATE  
@method_decorator(login_required, name='dispatch')
class CategoryUpdateView(generic.UpdateView):
    template_name = "master/category/category_create.html"
    form_class=CategoryForm
    queryset = Category.objects.all()
    context_object_name = "category"
    
    def get_success_url(self):
        return reverse("CategoryList")


# PRODUCT SUBCATEGORY CREATE
@method_decorator(login_required, name='dispatch')
# class SubCategoryCreateView(generic.CreateView):
#     template_name = 'master/category/sub_category_create.html'
#     form_class = SubCategoryForm

#     def get_success_url(self):
#         messages.success(self.request, 'Category Created Sucessfully')
#         return reverse("SubCategoryList")


# # PRODUCT SUBCATEGORY LIST
# @method_decorator(login_required, name='dispatch')
# class SubCategoryListView(generic.ListView):
#     template_name = "master/category/sub_category_list.html"
#     queryset = Category.objects.all()
#     context_object_name = "subcategory"
    
# PRODUCT SUBCATEGORY UPDATE
# @method_decorator(login_required, name='dispatch')
# class SubCategoryUpdateView(generic.UpdateView):
#     template_name = "master/category/sub_category_create.html"
#     form_class=SubCategoryForm
#     queryset = Category.objects.all()
#     context_object_name = "subcategory"
    
#     def get_success_url(self):
#         return reverse("SubCategoryList")


# PRODUCT BRAND CREATE
@method_decorator(login_required, name='dispatch')
class BrandCreateView(generic.CreateView):
    template_name = 'master/brand/brand_create.html'
    form_class = BrandForm

    def get_success_url(self):
        messages.success(self.request, 'Category Created Sucessfully')
        return reverse("BrandList")


# PRODUCT BRAND LIST
@method_decorator(login_required, name='dispatch')
class BrandListView(generic.ListView):
    template_name = "master/brand/brand_list.html"
    queryset = Brand.objects.all()
    context_object_name = "brand"
    
# PRODUCT BRAND UPDATE
@method_decorator(login_required, name='dispatch')
class BrandUpdateView(generic.UpdateView):
    template_name = "master/brand/brand_create.html"
    form_class=BrandForm
    queryset = Brand.objects.all()
    context_object_name = "brand"
    
    def get_success_url(self):
        return reverse("BrandList")


# SOFTWARE TYPE CREATE
@method_decorator(login_required, name='dispatch')
class SoftwareTypeCreateView(generic.CreateView):
    template_name = 'master/type/s_type_create.html'
    form_class = SoftwareTypeForm

    def get_success_url(self):
        messages.success(self.request, 'Category Created Sucessfully')
        return reverse("SoftwareTypeList")


# SOFTWARE TYPE LIST
@method_decorator(login_required, name='dispatch')
class SoftwareTypeListView(generic.ListView):
    template_name = "master/type/s_type_list.html"
    queryset = SoftwareType.objects.all()
    context_object_name = "s_type"
    
# SOFTWARE TYPE Update
@method_decorator(login_required, name='dispatch')
class SoftwareTypeUpdateView(generic.UpdateView):
    template_name = "master/type/s_type_create.html"
    form_class=SoftwareTypeForm
    queryset = SoftwareType.objects.all()
    context_object_name = "s_type"
    
    def get_success_url(self):
        return reverse("SoftwareTypeList")
