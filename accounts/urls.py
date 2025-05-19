from django.urls import path
from . import views

urlpatterns = [
    path("register/",views.register_view,name="register"),
    path("login/",views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path('dashboard/staff/', views.staff_dashboard_view, name='staff_dashboard'),
    path('dashboard/guest/', views.guest_dashboard_view, name='guest_dashboard'),
    path('manager/dashboard/', views.manager_dashboard_view, name='manager_dashboard'),
    path('manager/staff/', views.manager_staff_view, name='manager_staff'),
    path('manager/services/', views.manager_services_view, name='manager_services'),
]
