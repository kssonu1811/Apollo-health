from ticket_app1.views import home
from django.contrib import admin
from .models import Appointment

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id","first_name","last_name","email","phone","a_date_time")
    list_display_links = ("id","first_name","last_name")
    search_fields = ("first_name","last_name","email","phone")
    list_per_page = 25
admin.site.register(Appointment, AppointmentAdmin)

