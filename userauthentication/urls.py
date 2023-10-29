from django.contrib import admin
from django.urls import path, include
from .views import UserMVS
from rest_framework import routers


router = routers.DefaultRouter()
router.register("user", UserMVS)

urlpatterns = [
    path("", include(router.urls))
]