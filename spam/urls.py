from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.contrib import admin
from django.urls import path

from spam.views import Register


router = DefaultRouter()
router.register('register', Register, basename='register')



urlpatterns = [
    path('', include(router.urls)),
]
