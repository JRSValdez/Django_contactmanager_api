from contactmanager import views
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'contacts', views.ContactViewSet, 'contact')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls))
]
