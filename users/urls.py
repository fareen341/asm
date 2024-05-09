from django.urls import path
from users import views
from .views import (
    UserListView,
   
    UserCreateView,
    UserUpdateView,
)


urlpatterns = [

    path('list', UserListView.as_view(), name="UserList"),
    path('add', UserCreateView.as_view(), name="UserCreate"),
    path('<int:pk>/update', UserUpdateView.as_view(), name="UserUpdate"),
    # path('add', views.UserCreateView, name="UserCreate"),
    
    # path('<int:pk>', UserDetailView.as_view(), name="UserDetail"),
    path('<int:pk>', views.UserDetailView, name="UserDetail"),
    
    path('ajax/load-emp-location', views.load_empuser_location, name='ajax_load_empuserlocation'), # AJAX 
]

