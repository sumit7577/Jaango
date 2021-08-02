from django.urls import path
from app import views

urlpatterns = [
    # The home page
    path("",views.home,name="home"),
    path('register', views.index, name='register'),
    path("addProperty",views.addProperty,name="addProperty"),
    path("addStructure",views.addStructure,name="addStructure"),
    path("addFlat",views.addFlat,name="addFlat"),
    path("addMaterial",views.addMaterial,name="addMaterial"),
    path("addService",views.addService,name="addService"),
    path("addEquipment",views.addEquipment,name="addEquipment"),
    path("structure",views.structure,name="structure"),
    path("equipment",views.equipment,name="equipments"),
    path("services",views.services,name="services"),
    path("materials",views.material,name="material"),
    path("flats",views.flats,name="flats"),
    path("property",views.property,name="property"),
    path('login', views.login_view, name='login'),
    path("logout/", views.logou, name="logout"),
]
