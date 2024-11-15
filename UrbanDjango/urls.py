"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task2.views import index, index2
from task3.views import *
from task4.views import index_cart, index_primary, index_store
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('function/', index),
    path('class/', index2.as_view()),
    path('primary/', TemplateView.as_view(template_name = 'third_task/primary.html')),
    path('store/', TemplateView.as_view(template_name = 'third_task/store.html')),
    path('cart/', TemplateView.as_view(template_name = 'third_task/cart.html')),
    path('cart4/', index_cart),
    path('primary4/', index_primary),
    path('store4/', index_store)
]




