from django.contrib import admin

from .forms import BoulderForm
from .models import ClimbingWall, ClimbingWallPlace, Boulder, Tick


class BoulderAdmin(admin.ModelAdmin):
    form = BoulderForm
    fieldsets = (
        (None, {
            'fields': ('place', 'level', 'color')
            }),
        )
    list_display = ('__unicode__',)


class ClimbinWallAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)


class ClimbingWallPlaceAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)


class TickAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)

admin.site.register(ClimbingWall, ClimbinWallAdmin)
admin.site.register(ClimbingWallPlace, ClimbingWallPlaceAdmin)
admin.site.register(Boulder, BoulderAdmin)
admin.site.register(Tick, TickAdmin)
