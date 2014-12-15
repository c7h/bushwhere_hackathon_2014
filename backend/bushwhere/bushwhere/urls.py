from django.conf.urls import patterns, include, url

from api import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bushwhere.views.home', name='home'),
    # url(r'^bushwhere/', include('bushwhere.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('api.urls')),

	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    url(r'^next$', views.next_place),
    url(r'^visit$', views.visit),
)

