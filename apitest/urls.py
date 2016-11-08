from django.conf.urls import include, url
from django.contrib import admin
from apitest import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'sccapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', views.index, name='index'),
    url(r'^instance/$', views.get_instance, name='get_instance'),
    #url(r'^instance/result', views.return_instance, name='return_instance'),
    url(r'^instance/result', views.sccapi_get, name='return_instance'),
]
