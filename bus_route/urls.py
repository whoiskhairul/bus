from django.contrib import admin
from django.urls import path,include
from user_info import views
urlpatterns = [
    path('khairul/', admin.site.urls),
    path('signup/',views.user_signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('bus/',include('user_info.urls'),name='bus'),
    path('map/',include('map.urls')),
    path('',views.index, name = 'index')

]
