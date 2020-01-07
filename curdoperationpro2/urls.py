"""curdoperationpro2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from curdapp2 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.Home_view),
    path('create/', views.Create_view),
    path('retrieve/', views.Retrieve_view),
    path('update/', views.Update_view),
    path('delete/', views.Delete_view),
    path('home/', views.Home_view),
]
