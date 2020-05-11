from django.contrib import admin
from django.urls import path,include
from user_info import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',views.user_login,name='login'),
    path('bus/',include('user_info.urls'),name='user'),
    path('map/',include('map.urls'),name='map'),
    path('',views.index, name = 'index')

]
