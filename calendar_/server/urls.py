from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from core import views
from event.views import EventView, RequestView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'event', EventView, basename='event')
router.register(r'request', RequestView)


urlpatterns = [
    path('', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    path('hello/', views.home, name='home'),
    path('signup/', views.sign_up, name='signup'), # <= sign up route 
    path('logout/', views.log_out, name='logout'),
    path('login/', views.log_in, name='login'), # <= log in route
]

