from django.contrib import admin

# Register your models here.
from .models import Event, Booking, Category, Contact

admin.site.register(Event)
admin.site.register(Booking)
admin.site.register(Category)
admin.site.register(Contact)