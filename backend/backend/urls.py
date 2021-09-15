from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r"", views.NoteViewSet, "")

urlpatterns = [path("admin/", admin.site.urls), path("", include(router.urls))]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
