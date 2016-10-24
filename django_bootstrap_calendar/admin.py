from django.contrib import admin
from .models import CalendarEvent
from .forms import EventForm

admin.site.register(CalendarEvent)

class CreateEvent(admin.ModelAdmin):
    form = EventForm
    fields = ('title', 'css_class', 'start', 'end', 'zID', 'notes', 'apptType', 'ugc',)

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()