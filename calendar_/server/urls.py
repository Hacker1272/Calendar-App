from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('hello/', views.home, name='home'),
    path('signup/', views.sign_up, name='signup'), # <= sign up route 
    path('logout/', views.log_out, name='logout'),
    path('login/', views.log_in, name='login'), # <= log in route
]

