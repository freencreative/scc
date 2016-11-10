from django.conf.urls import include, url
from django.contrib import admin
from apitest import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'sccapi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^apitest/', include('apitest.urls', namespace="apitest")),
    url(r'^nurione/', include('nurione.urls', namespace="nurione")),
    url(r'^admin/', include(admin.site.urls)),
]
