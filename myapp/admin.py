from django.contrib import admin
from .models import Contact,User,Doctor_profile,Appointment,cancelappointment,Healthprofile
# Register your models here.
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Doctor_profile)
admin.site.register(Appointment)
admin.site.register(cancelappointment)
admin.site.register(Healthprofile)