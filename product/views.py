from django.shortcuts import get_object_or_404, render, reverse, redirect, HttpResponseRedirect  # type: ignore
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib import messages
from .models import (Software, Hardware,Nonitasset)
from users.models import User
from master.models import Category,Location
from .forms import (SoftwareForm, HardwareUpdateForm,HardwareDetailForm, HardwareAssignForm, HardwareCreateForm, HardwareReturnForm,NonITAssetCreateForm,NonITAssetUpdateForm,NonITAssetAssignForm,NonITAssetReturnForm)


# SOFTWARE PRODUCT CREATE
@method_decorator(login_required, name='dispatch')
class SoftwareCreateView(generic.CreateView):
    template_name = 'product/software/software_create.html'
    form_class = SoftwareForm

    def get_success_url(self):
        messages.success(self.request, 'Software Created Sucessfully')
        return reverse("SoftwareList")


# SOFTWARE PRODUCT LIST
@method_decorator(login_required, name='dispatch')
class SoftwareListView(generic.ListView):
    template_name = "product/software/software_list.html"
    queryset = Software.objects.all()
    context_object_name = "software"
    
# SOFTWARE PRODUCT Update
@method_decorator(login_required, name='dispatch')
class SoftwareUpdateView(generic.UpdateView):
    template_name = "product/software/software_update.html"
    form_class=SoftwareForm
    queryset = Software.objects.all()
    context_object_name = "software"
    
    def get_success_url(self):
        return reverse("SoftwareList")



# HARDWARE PRODUCT CREATE
# @method_decorator(login_required, name='dispatch')
# class HardwareCreateView(generic.CreateView):
#     template_name = 'product/hardware/hardware_create.html'
#     form_class = HardwareCreateForm

#     def get_success_url(self):
#         messages.success(self.request, 'Hardware Created Sucessfully')
#         return reverse("HardwareList")


@login_required
def HardwareCreateView(request):
    form = HardwareCreateForm(request.POST or None)  
    if form.is_valid():
        # form.asset_type= Hardware.objects.update(asset_type='IT Assets')
        form.save()
        return redirect("HardwareList")
    context={
        "form":form
    }
        
    return render(request,'product/hardware/hardware_create.html',context)
    


# HARDWARE PRODUCT LIST
@method_decorator(login_required, name='dispatch')
class HardwareListView(generic.ListView):
    template_name = "product/hardware/hardware_list.html"
    queryset = Hardware.objects.all().exclude(status='disposed')

    context_object_name = "hardware"
    
    # HARDWARE PRODUCT UPDATE
@method_decorator(login_required, name='dispatch')
class HardwareUpdateView(generic.UpdateView):
    template_name = "product/hardware/hardware_update.html"
    form_class=HardwareUpdateForm
    queryset = Hardware.objects.all()
    context_object_name = "hardware"
    
    def get_success_url(self):
        return reverse("HardwareList")
    
    
# @method_decorator(login_required, name='dispatch') 
# class UnAssignedView(generic.ListView):
#     template_name = "product/hardware/hardware_unassigned_list.html"
#     # queryset = Product.objects.raw('Select * From product_product Where "assign_to_id" IS NULL')
#     queryset = Hardware.objects.filter(assigned_to__id = None)
#     context_object_name = "hardware"

# @method_decorator(login_required, name='dispatch')    
# class AssignedView(generic.ListView):
#     template_name = "product/hardware/hardware_assigned_list.html"
#     # queryset = Product.objects.raw('Select * From product_product Where NOT (assign_to_id=None)
#     queryset = Hardware.objects.exclude(assigned_to__id = None)
#     context_object_name = "hardware"

@login_required
def AssignedView(request):
    # sql = "SELECT product_hardware.id, product_hardware.name, product_hardware.assigned_to_id, users_user.username, master_location.location FROM ((product_hardware INNER JOIN users_user ON users_user.id=product_hardware.assigned_to_id)INNER JOIN master_location ON master_location.id=users_user.location_id  ) WHERE product_hardware.assigned_to_id IS NOT NULL"
    # abc="WHERE assigned_to_id  IS NOT NULL"
    # sql2 = ""
    # sql3 = sql+sql2
    # pkid= Hardware.objects.raw(sql) 
    pkid= Hardware.objects.exclude(assigned_to__id = None)
    
    print(pkid)
    context ={
               "hardware":pkid,
         }
    return render(request,'product/hardware/hardware_assigned_list.html',context)
    
    
       # HARDWARE PRODUCT Assign
@method_decorator(login_required, name='dispatch')
class HardwareAssignView(generic.UpdateView):
    template_name = "product/hardware/hardware_assign.html"
    form_class=HardwareAssignForm
    queryset = Hardware.objects.all()
    context_object_name = "hardware"
    
    def get_success_url(self):
        return reverse("AssignAsset")


@login_required
def HardwareDetailView(request,pk):
    pkid= Hardware.objects.get(id=pk)
    soft= Software.objects.filter(installed_on=pkid)
    
    # locate=Location.objects.filter(location=pkid)
    # locate= Location.objects.filter(=pkid)
    
    form = HardwareAssignForm(request.POST or None, instance=pkid)  
    form2 = HardwareReturnForm(request.POST or None, instance=pkid)  
    if form.is_valid():
        form.save()
    if form2.is_valid():
        form2.save()
        # return HttpResponseRedirect("/"+pkid)
    context ={
        "form": form,
        "form2": form2,
        "hardware":pkid,
        "software":soft,
        # "location":locate,
        
    }
    return render(request,'product/hardware/hardware_detail.html',context)

@login_required
def load_category(request):
    category_id = request.GET.get('category_id')
    subcategory = Category.objects.filter(category_id=category_id)
    return render(request, 'product/hardware/subcategory_dropdown_list.html', {'subcategory': subcategory})

@login_required
def load_location(request):
    user_id = request.GET.get('id_assigned_to')
    print(user_id)
    
    # location=User.objects.raw("SELECT users_user.id,users_user.location_id  From users_user WHERE users_user.id=%s ",[user_id])
  
    # useloc=Location.objects.filter(id=location)
    location= Location.objects.all()
    print (location)
    return render(request, 'product/hardware/location_dropdown_list.html', {'location': location})



@login_required
def load_emp_location(request):
    branch_id = request.GET.get('branch_id')
    location = Location.objects.filter(branch_id=branch_id).filter(location_type='Asset Location')
    return render(request, 'product/hardware/location_dropdown_list.html', {'location': location})


@login_required
def load_assignuser_location(request):
    userloc_id = request.GET.get('userlocation_id')
    # user=User.objects.raw("Select users_user.location_id From prodcut_hardware ,users_user WHERE product_hardware.assigned_to_id =%s",[userloc_id])
    user=User.objects.filter(id=userloc_id)
    print(user)
    location = Location.objects.filter(user__in=User.objects.filter(id=userloc_id))
    print(location)
    # .filter(location_type='Employee Location')
    # user_id=User.objects.filter(id=location_id)
    # print(user_id)
    # user=User.objects.raw("Select users_user.location_id From prodcut_hardware users_user WHERE product_hardware.assigned_to_id =%s",[user_id])
    # print(user)
    # self.fields['location'].queryset = Location.objects.filter(location=user)
    return render(request, 'product/hardware/location_dropdown_list.html', {'location': location})

    
    
    
#*****************************************Report Views*********************************

# AssignedAssetReportListView

@method_decorator(login_required, name='dispatch')
class AssignedAssetReportListView(generic.ListView):
    template_name = "product/hardware/hardware_assigned_list.html"
    queryset = Hardware.objects.exclude(assigned_to__id=None)

    context_object_name = "hardware"
    
    
# UnAssignedAssetReportListView
@method_decorator(login_required, name='dispatch')
class UnAssignedAssetReportListView(generic.ListView):
    template_name = "product/hardware/hardware_unassigned_list.html"
    queryset = Hardware.objects.filter(assigned_to__id=None).exclude(status='disposed')

    context_object_name = "hardware"


# DisposedAssetListView
@method_decorator(login_required, name='dispatch')
class DisposedAssetListView(generic.ListView):
    template_name = "product/hardware/hardware_disposedasset.html"
    queryset = Hardware.objects.filter(status='disposed')

    context_object_name = "hardware"
    
    
# SoftwareInUseListView
@method_decorator(login_required, name='dispatch')
class SoftwareInUseListView(generic.ListView):
    template_name = "product/software/software_inuse_list.html"
    queryset = Software.objects.exclude(installed_on__id=None)

    context_object_name = "software"
    
# SoftwareInStockListView    
@method_decorator(login_required, name='dispatch')
class SoftwareInStockListView(generic.ListView):
    template_name = "product/software/software_instock_list.html"
    queryset = Software.objects.filter(installed_on__id=None)

    context_object_name = "software"
    
    
    
    
# *********************NON IT ASSET VIEWS************************************



class NonITAssetAssignView(generic.UpdateView):
    pass



# NON IT ASSET PRODUCT Create
@login_required
def NonITAssetCreateView(request):
    form = NonITAssetCreateForm(request.POST or None)  
    if form.is_valid():
        form.save()
        return redirect("NonITAssetList")
    context={
        "form":form
    }
        
    return render(request,'product/nonitasset/nonitasset_create.html',context)
    


# NON IT ASSET PRODUCT LIST
# @method_decorator(login_required, name='dispatch')
class NonITAssetListView(generic.ListView):
    
    template_name = "product/nonitasset/nonitasset_list.html"
    queryset = Nonitasset.objects.all()

    context_object_name = "hardware"
    
    # NON IT ASSET PRODUCT UPDATE
# @method_decorator(login_required, name='dispatch')
class NonITAssetUpdateView(generic.UpdateView):
    
    template_name = "product/nonitasset/nonitasset_update.html"
    form_class=NonITAssetUpdateForm
    queryset = Nonitasset.objects.all()
    context_object_name = "hardware"
    
    def get_success_url(self):
        return reverse("NonITAssetList")
    
    
    
@login_required
def NonITAssetDetailView(request,pk):
    pkid= Nonitasset.objects.get(id=pk)
    # soft= Software.objects.filter(installed_on=pkid)
    
    # locate=Location.objects.filter(location=pkid)
    # locate= Location.objects.filter(=pkid)
    
    form = NonITAssetAssignForm(request.POST or None, instance=pkid)  
    form2 = NonITAssetReturnForm(request.POST or None, instance=pkid)  
    if form.is_valid():
        form.save()
    if form2.is_valid():
        form2.save()
        # return HttpResponseRedirect("/"+pkid)
    context ={
        "form": form,
        "form2": form2,
        "hardware":pkid,
        # "software":soft,
        # "location":locate,
        
    }
    return render(request,'product/nonitasset/nonitasset_detail.html',context)