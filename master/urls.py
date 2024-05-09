from django.urls import path
from users import views
from .views import (

    CompanyCreateView,
    CompanyListView,
    CompanyUpdateView,
    
    BranchCreateView,
    BranchListView,
    BranchUpdateView,
    
    EmployeeLocationCreateView,
    EmployeeLocationListView,
    ElocationUpdateView,
    
    VendorCreateView,
    VendorListView,
    VendorUpdateView,
    
    CategoryCreateView,
    CategoryListView,
    CategoryUpdateView,
    
    
    
    BrandCreateView,
    BrandListView,
    BrandUpdateView,
   
    SoftwareTypeCreateView,
    SoftwareTypeListView,
    SoftwareTypeUpdateView
)

# SubCategoryCreateView,
#     SubCategoryListView,
#     SubCategoryUpdateView,
#         AssetLocationCreateView,
#     AssetLocationListView,
#     AssetLocationUpdateView,

urlpatterns = [
    path('company', CompanyCreateView.as_view(), name="CompanyCreate"),
    path('company_list', CompanyListView.as_view(), name="CompanyList"),
    path('company/update/<int:pk>',CompanyUpdateView.as_view(), name="CompanyUpdate"),
    
    path('branch', BranchCreateView.as_view(), name="BranchCreate"),
    path('branch/update/<int:pk>',BranchUpdateView.as_view(), name="BranchUpdate"),
    path('branch_list', BranchListView.as_view(), name="BranchList"),
    
    path('employee_location', EmployeeLocationCreateView.as_view(),name="EmployeeLocationCreate"),
    path('location_list', EmployeeLocationListView.as_view(), name="EmployeeLocationList"),
    path('employee_location/update/<int:pk>', ElocationUpdateView.as_view(), name="E_locationUpdate"),
    
    path('vendor', VendorCreateView.as_view(), name="VendorCreate"),
    path('vendor_list', VendorListView.as_view(), name="VendorList"),
    path('vendor/update/<int:pk>', VendorUpdateView.as_view(), name="VendorUpdate"),
    
    # path('asset_location', AssetLocationCreateView.as_view(), name="AssetLocationCreate"),
    # path('asset_location_list', AssetLocationListView.as_view(), name="AssetLocationList"),
    # path('asset_location/update/<int:pk>', AssetLocationUpdateView.as_view(), name="AssetLocationUpdate"),
    
    
    
    path('category', CategoryCreateView.as_view(), name="CategoryCreate"),
    path('category_list', CategoryListView.as_view(), name="CategoryList"),
    path('category/update/<int:pk>', CategoryUpdateView.as_view(), name="CategoryUpdate"),
    
    # path('subcategory', SubCategoryCreateView.as_view(), name="SubCategoryCreate"),
    # path('subcategory_list', SubCategoryListView.as_view(), name="SubCategoryList"),
    # path('subcategory/update/<int:pk>', SubCategoryUpdateView.as_view(), name="SubCategoryUpdate"),
    
    path('brand', BrandCreateView.as_view(), name="BrandCreate"),
    path('brand_list', BrandListView.as_view(), name="BrandList"),
    path('brand/update/<int:pk>', BrandUpdateView.as_view(), name="BrandUpdate"),
    
    path('software_type', SoftwareTypeCreateView.as_view(), name="SoftwareTypeCreate"),
    path('software_type_list', SoftwareTypeListView.as_view(), name="SoftwareTypeList"),
    path('software_type/update/<int:pk>', SoftwareTypeUpdateView.as_view(), name="SoftwareTypeUpdate"),
    
]


