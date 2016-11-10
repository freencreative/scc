from django.conf.urls import include, url
from django.contrib import admin
from nurione import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'sccapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]
