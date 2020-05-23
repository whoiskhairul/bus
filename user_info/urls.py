from django.urls import path
from user_info import views

urlpatterns = [
    path('',views.show_user_info,name='bus-info'),
    
    path('logout',views.user_logout,name='logout'),
    
    path('<bus_name>' , views.show_bus_info, name = 'bus-name'),

]
