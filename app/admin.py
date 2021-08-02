from django.contrib import admin
from .models import UserDetails,Files,Property,Structure,Equipment,Material,Service,Flat
# Register your models here.
admin.site.register(UserDetails)
admin.site.register(Files)
admin.site.register(Property)
admin.site.register(Structure)
admin.site.register(Equipment)
admin.site.register(Material)
admin.site.register(Service)
admin.site.register(Flat)
