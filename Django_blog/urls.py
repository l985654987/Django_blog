"""Django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login, name='blog_login'),
    url(r'^reg/', views.reg, name='blog_reg'),
    url(r'^home/', views.home, name='blog_home'),
    url(r'^add/', views.add, name='blog_add'),
    url(r'^edit/(?P<id>\d+)/', views.edit, name='blog_edit'),
    url(r'^del/(?P<id>\d+)/', views.delete, name='blog_del'),
    url(r'^logout/', views.logout, name='blog_logout'),
    url(r'^myblogs/', views.myblogs, name='my_blogs'),
    url(r'^content/(?P<id>\d+)/', views.content, name='blog_content'),
    url(r'^sort_blog/(?P<str>\D+)/', views.sortblog, name='sort_blog'),
    url(r'^$', views.home)

]
