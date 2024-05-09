from django.urls import path
from users import views
from product import views

from .views import (SoftwareCreateView, SoftwareListView,
                    HardwareListView,SoftwareUpdateView,HardwareUpdateView,HardwareAssignView,
                    HardwareDetailView,AssignedAssetReportListView,UnAssignedAssetReportListView,
                    DisposedAssetListView,SoftwareInUseListView,SoftwareInStockListView,NonITAssetListView,
NonITAssetUpdateView,NonITAssetAssignView,
# UnAssignedView,
)

urlpatterns = [
    path('software', SoftwareCreateView.as_view(), name="SoftwareCreate"),
    path('software_list', SoftwareListView.as_view(), name="SoftwareList"),
    path('software/update/<int:pk>', SoftwareUpdateView.as_view(), name="SoftwareUpdate"),
    
    
    path('hardware', views.HardwareCreateView, name="HardwareCreate"),
    path('hardware_list', HardwareListView.as_view(), name="HardwareList"),
    path('hardware/update/<int:pk>', HardwareUpdateView.as_view(), name="HardwareUpdate"),
    # path('hardware/detail/<int:pk>', HardwareDetailView.as_view(), name="HardwareDetail"),
    path('hardware/detail/<int:pk>', views.HardwareDetailView, name="HardwareDetail"),
    path('hardware/assign/<int:pk>', HardwareAssignView.as_view(), name="HardwareAssign"),
    # path('hardware/return/<int:pk>', HardwareReturnView.as_view(), name="HardwareReturn"),
    # path('hardware/return/<int:pk>', views.HardwareReturn, name="HardwareReturn"),
    
    
    path('assignassets', views.AssignedView, name="AssignAsset"),
    # path('unassignassets', UnAssignedView.as_view(), name="UnAssignAsset"),
    
    path('ajax/load-category', views.load_category, name='ajax_load_category'), # AJAX
    path('ajax/load-location', views.load_location, name='ajax_load_location'), # AJAX
    path('ajax/load-emp-location', views.load_emp_location, name='ajax_load_emplocation'), # AJAX
    path('ajax/load-assignuser-location', views.load_assignuser_location, name='ajax_load_assignuserlocation'), # AJAX
    
    
    
    #Reports
    path('hardware_assigned-asset',AssignedAssetReportListView.as_view(), name="AssignedAssetReport"),
    path('hardware_unassigned-asset',UnAssignedAssetReportListView.as_view(), name="UnAssignedAssetReport"),
    path('hardware-disposed-asset', DisposedAssetListView.as_view(), name="DisposedAsset"),
    path('software-in-use', SoftwareInUseListView.as_view(), name="SoftwareInUse"),
    path('software-in-stock', SoftwareInStockListView.as_view(), name="SoftwareInStock"),
    
    path('non-it-assets', views.NonITAssetCreateView, name="NonITAssetCreate"),
    path('non-it-assets-list', NonITAssetListView.as_view(), name="NonITAssetList"),
    path('non-it-assets/update/<int:pk>', NonITAssetUpdateView.as_view(), name="NonITAssetUpdate"),
    # path('hardware/detail/<int:pk>', HardwareDetailView.as_view(), name="HardwareDetail"),
    path('non-it-asset/detail/<int:pk>',views.NonITAssetDetailView, name="NonITAssetDetail"),
    path('non-it-assets/assign/<int:pk>', NonITAssetAssignView.as_view(), name="NonITAssetAssign"),
    # path('hardware/return/<int:pk>', HardwareReturnView.as_view(), name="HardwareReturn"),
    # path('hardware/return/<int:pk>', views.HardwareReturn, name="HardwareReturn"),
]
