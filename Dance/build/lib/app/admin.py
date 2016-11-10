from django.contrib import admin
from app.models import UpComingEvents
# Register your models here.


class UpComingEventAdmin(admin.ModelAdmin):
    list_display = ('EventDate', 'EventVenue', 'EventImage', 'EventOrganiser', 'ShowCategory', 'EventContact','EventLink')
    list_filter = ('EventDate', 'EventVenue')


admin.site.register(UpComingEvents, UpComingEventAdmin)