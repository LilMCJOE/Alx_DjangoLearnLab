from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions



urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/', include('posts.urls')),
]
