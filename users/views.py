from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, reverse, redirect    # type: ignore
from django.views import generic
from django.contrib import messages
from users.models import (User, Company,Location)
from .forms import (CreateUser, UpdateUser, CompanyForm)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from product.models import Hardware, Software,Nonitasset
from master.models import Category
from django.db.models import Count, Sum


# User Create View
@method_decorator(login_required, name='dispatch')
class UserCreateView(generic.CreateView):
    template_name = 'user/user_create.html'
    form_class = CreateUser

    def get_success_url(self):
        messages.success(self.request, 'User Created Sucessfully')
        return reverse("UserList")
    
# User List View

@method_decorator(login_required, name='dispatch')
class UserListView(generic.ListView):
    template_name = "user/user_list.html"
    queryset = User.objects.all()
    context_object_name = "user"

# User Detail View


# @method_decorator(login_required, name='dispatch')
# class UserDetailView(generic.DetailView):
#     template_name = "user/user_detail.html"
#     model = User

#     def get_context_data(self, *args,  **kwargs):
#         user = User.objects.all()
#         context = super(UserDetailView, self,
#                         ).get_context_data(*args, **kwargs)
#         profile = get_object_or_404(User, id=self.kwargs['pk'])

#         # context[profile] = profile
#         return context

@login_required
def UserDetailView(request,pk):
    userpk=User.objects.get(id=pk)
    print(userpk)
    
    pkid= Hardware.objects.filter(assigned_to_id=userpk)
    print(pkid)
        
    context ={
        "user":userpk,
        "hardware":pkid,
        }
    return render(request,'user/user_detail.html',context)
    

# User Update View

@method_decorator(login_required, name='dispatch')
class UserUpdateView(generic.UpdateView):
    template_name = "user/user_update.html"
    form_class = UpdateUser
    queryset = User.objects.all()
    context_object_name = "user"

    def get_success_url(self):
        return reverse("UserList")


# User Login view

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Dashboard')
        else:
            messages.info(request, 'Username Or Password Is Incorrect')

    context = {}
    return render(request, 'registration/login.html', context)


# User Logout View

def LogoutUser(request):
    logout(request)
    return redirect('Login')





@login_required
def load_empuser_location(request):
    branch_id = request.GET.get('branch_id')
    location = Location.objects.filter(branch_id=branch_id).filter(location_type='Employee Location')
    print(location)
    return render(request, 'user/location_dropdown_list.html', {'location': location})





def Dashboard(request):
    it_asset = Hardware.objects.filter(asset_type='IT Assets')
    it_asset_count =it_asset.count()    
    non_it_asset = Nonitasset.objects.filter(asset_type='NON IT Assets')
    non_it_asset_count =non_it_asset.count()
    software = Software.objects.all()
    software_count =software.count()
    employee = User.objects.all()
    employee_count =employee.count()
    in_stock = Hardware.objects.filter(assigned_to__id = None)
    in_stock_count =in_stock.count()    
    assign = Hardware.objects.exclude(assigned_to__id = None)
    assign_count =assign.count()
    working = Hardware.objects.filter(status = 'working')
    working_count =working.count()
    year = Hardware.objects.values('purchased_on__year').annotate(total=Count('id')).values_list('purchased_on__year', flat=True)
    count = Hardware.objects.filter(purchased_on__year='2022').aggregate(Sum('cost'))
    year_count = Hardware.objects.values('purchased_on__year').annotate(total=Count('id')).values_list('total', flat=True)
    soft_year = Software.objects.values('purchased_on__year').annotate(total=Count('id')).values_list('purchased_on__year', flat=True)
    soft_year_count = Software.objects.values('purchased_on__year').annotate(total=Count('id')).values_list('total', flat=True)

    
    it_asset_cat1 = Hardware.objects.filter(asset_type='IT Assets').values('category').annotate(total=Count('id')).values_list('category', flat=True)
    it_asset_cat = Category.objects.filter(id__in=it_asset_cat1)
    it_asset_cat_count = Hardware.objects.filter(asset_type='IT Assets').values('category').annotate(total=Count('id')).values_list('total', flat=True)

    non_it_asset_cat1 = Nonitasset.objects.filter(asset_type='NON IT Assets').values('category').annotate(total=Count('id')).values_list('category', flat=True)
    non_it_asset_cat = Category.objects.filter(id__in=non_it_asset_cat1)
    non_it_asset_cat_count = Nonitasset.objects.filter(asset_type='NON IT Assets').values('category').annotate(total=Count('id')).values_list('total', flat=True)

    context = {
        #DATA
         'in_stock'     : in_stock,
         'it_asset'     : it_asset,
         'non_it_asset' : non_it_asset,
         'software'     : software,
         'assign'       : assign,
         'employee'     : employee,
         'working'      : working,
         'year'         : year,
         'count':count,
         'soft_year'         : soft_year,
         'it_asset_cat':it_asset_cat,
         'non_it_asset_cat':non_it_asset_cat,
         
         
         #COUNT
         'it_asset_cat_count':it_asset_cat_count,
         'non_it_asset_cat_count':non_it_asset_cat_count,
         'in_stock_count'       : in_stock_count,
         'it_asset_count'       : it_asset_count,
         'non_it_asset_count'   : non_it_asset_count,
         'software_count'       : software_count,
         'assign_count'         : assign_count,
         'employee_count'       : employee_count,
         'working_count'        : working_count,
         'year_count'           : year_count,
         'soft_year_count'           : soft_year_count
     }
    context["in_stock"] = Hardware.objects.exclude(assigned_to__id = None)
    context["assign"] = Hardware.objects.filter(assigned_to__id = None)
    
    return render(request,'dashboard/dashboard.html', context)
