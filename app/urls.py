from app.forms2 import contact
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
    path("property/<str:id>",views.propertyView,name="propertyView"),
    path("editProperty/<str:id>",views.editProperty,name="editProperty"),
    path("structure/<str:id>",views.structureView,name="structureView"),
    path("editStructure/<str:id>",views.editStructure,name="editStructure"),
    path("materials/<str:id>",views.materialView,name="materialView"),
    path("editMaterial/<str:id>",views.editMaterial,name="editMaterial"),
    path("flats/<str:id>",views.flatView,name="flatView"),
    path("equipment/<str:id>",views.equipmentView,name="equipmentView"),
    path("services/<str:id>",views.serviceView,name="serviceView"),
    path("editService/<str:id>",views.editService,name="editService"),
    path("profile",views.profile,name="profile"),
]
