from django.contrib import admin
from .models import UserDetails,Files,Property,Structure,Equipment,Material,Service,Flat,PropertyIMage,StructureImage,EquipmentImage,MaterialImage,ServiceImage,FlatImage
# Register your models here.
admin.site.register(UserDetails)
admin.site.register(Files)
admin.site.register(Property)
admin.site.register(Structure)
admin.site.register(Equipment)
admin.site.register(Material)
admin.site.register(Service)
admin.site.register(Flat)
admin.site.register(PropertyIMage)
admin.site.register(StructureImage)
admin.site.register(EquipmentImage)
admin.site.register(MaterialImage)
admin.site.register(ServiceImage)
admin.site.register(FlatImage)
