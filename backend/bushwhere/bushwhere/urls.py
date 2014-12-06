from django.conf.urls import patterns, include, url
from rest_framework import routers

from api import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'players', views.PlayerViewSet)
router.register(r'places', views.PlaceViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bushwhere.views.home', name='home'),
    # url(r'^bushwhere/', include('bushwhere.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

	# Wire up our API using automatic URL routing.
	# Additionally, we include login URLs for the browsable API.
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^next$', views.next_place),
)

