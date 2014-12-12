from django.contrib import admin
from models import Place, Player, Hint, Visit, Mission


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
	list_display = ('player', 'place')

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
	list_display = ('name', 'description')


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')


@admin.register(Hint)
class HintAdmin(admin.ModelAdmin):
	list_display = ('id', 'place')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
	list_display = ('name', 'lat', 'lon')
