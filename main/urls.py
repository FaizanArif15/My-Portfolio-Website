from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin', admin.site.urls),  # This should come FIRST
    path('', views.home, name='home'),
]


