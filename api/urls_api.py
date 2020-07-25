
from django.contrib import admin
from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from .views import UserViewSet,categories,leads

routers = routers.DefaultRouter()
routers.register('users',UserViewSet)
#routers.register('categories',categories)





urlpatterns = [
    path('', include(routers.urls)),
    path('categories/', categories),
    path('leads/', leads),
    
]
