"""blog URL Configuration

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
from XYZblog import views
from django.views.static import serve
from blog.settings import MEDIA_ROOT
import blog.settings

handler404 = "XYZblog.views.page_not_found"
handler500 = "XYZblog.views.page_error"

urlpatterns = [
    url(r'uploadIMG/',views.uploadIMG,name='uploadIMG'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT, }),
    url(r'^admin/',admin.site.urls),
    url(r'^$',views.listblogs,name='blog_get_blogs'),
    url(r'^detail/(\d+)/$',views.get_detail,name='blog_get_detail'),
    url(r'^(\d+)/$', views.listblogs, name='class_get_blogs'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': blog.settings.STATIC_ROOT }),
    
]