from django.contrib import admin
from django.utils.safestring import mark_safe

from .forms import BoulderForm, TickForm
from .models import ClimbingWall, ClimbingWallPlace, Boulder, Tick


class BoulderAdmin(admin.ModelAdmin):
    form = BoulderForm
    fieldsets = (
        (None, {
            'fields': ('place', 'level', 'color')
            }),
        )
    list_display = ('level', 'level_colored', 'place', 'color')

    def level_colored(self, obj):
        return mark_safe(
            '<span width=100% style="display: block; background:{};">{}</span>'.format(
                obj.color, obj.level))


class ClimbingWallAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ClimbingWallPlaceAdmin(admin.ModelAdmin):
    list_display = ('place', 'climbing_wall')


class TickAdmin(admin.ModelAdmin):
    form = TickForm
    list_display = ('level', 'level_colored', 'date', 'tries', 'success')

    def level(self, tick):
        return tick.boulder.place.place + " " + tick.boulder.level

    def level_colored(self, obj):
        return mark_safe(
            '<span width=100% style="display: block; background:{};"> </br> </span>'.format(
                obj.boulder.color))

admin.site.register(ClimbingWall, ClimbingWallAdmin)
admin.site.register(ClimbingWallPlace, ClimbingWallPlaceAdmin)
admin.site.register(Boulder, BoulderAdmin)
admin.site.register(Tick, TickAdmin)
