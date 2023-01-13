from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ConcertModel)
admin.site.register(LocationModel)
admin.site.register(TimeModel)
admin.site.register(TicketModel)
admin.site.register(ProfileModel)