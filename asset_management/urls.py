from django.contrib import admin
from django.urls import path, include
from users import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LoginPage, name="Login"),
    path('logout/', views.LogoutUser, name="Logout"),
    path('user/', include('users.urls')),
    path('master/', include('master.urls')),
    path('product/', include('product.urls')),
    path('dashboard/', views.Dashboard,name='Dashboard'),
]
