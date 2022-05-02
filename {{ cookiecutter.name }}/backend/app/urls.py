from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from .api_routers import router

urlpatterns = [path("admin/", admin.site.urls), path("api/", include(router.urls))]

if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
