from django.conf.urls import patterns, include, url
from rest_framework import routers

import views

router = routers.DefaultRouter()

router.register(r'players', views.PlayerViewSet)
router.register(r'places', views.PlaceViewSet)
router.register(r'missions', views.MissionViewSet)
router.register(r'visits', views.VisitViewSet)


urlpatterns = patterns('',

    url(r'^next$', views.next_place),
    url(r'^visit$', views.visit),
    url(r'^', include(router.urls)),
)