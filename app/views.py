from django.contrib.auth import authenticate, logout, login
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.utils.regex_helper import ESCAPE_MAPPINGS
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import Files, Flat, UserDetails, Property, Structure, Equipment, Material, Service, PropertyIMage, FlatImage, ServiceImage, EquipmentImage, StructureImage, MaterialImage,Contact,SMTP
from .forms2 import contact, propertyForm, Structure, Equipment, Material, Service, Flatform
from app import models
from app import forms2
from django.core.mail import send_mail

message = None
host_email =None
host_password = None
try:
    data = SMTP.objects.get(id=1)
    host_email = data.email
    host_password = data.password
except:
    message = "No smtp gmail added"
# Create your views here.
currency = Property.currency
pType = Property.propertyChoices
sale = Property.type

def index(request):
    form = SignUpForm(request.POST or None)
    msg = None

    if request.method == "POST":
        if form.is_valid():
            form.save()
            mobile = form.cleaned_data.get("mobile")
            userType = form.cleaned_data.get("userType")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            users = authenticate(username=username, password=password)
            UserDetails.objects.update_or_create(
                user=users, mobile=mobile, userType=userType)

            if users is not None:
                return redirect("/")
            else:
                msg = "Invalid Credentials"
        else:
            msg = "Error Validating the Form"

    return render(request, "sign-up.html", {"form": form, "message": msg})



def home(request):
    message = None
    success = False
    data = {}
    data["ptype"] = pType
    data["mtype"] = models.Material.type
    data["stype"] = models.Service.serviceType
    data["etype"] = models.Equipment.type
    property =Property.objects.all().count()
    sharedFlat = Flat.objects.filter(Type="Sale").count()
    rentFlat = Flat.objects.filter(Type="Rent").count()
    material = models.Material.objects.all().count()
    equipment = models.Equipment.objects.all().count()
    data["property"] = property
    data["rentFlat"] = sharedFlat
    data["sharedFlat"]= rentFlat
    data["material"]= material
    data["equipment"]=equipment
   
    if request.method == "POST":
        document = request.FILES.getlist("files")
        for i in document:
            Files.objects.create(userName=request.user, files=i)
        message = "Documents Successfully Published"
        success = True
    data["message"] = message
    data["success"] = success
    return render(request, "dashboard.html", data)


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "sign-in.html", {"form": form, "msg": msg})

def profile(request):
    return render(request,"profile.html")



def property(request):
    newList = []
    data = {}
    data["currency"] = currency
    data["ptype"] = pType
    data["fori"] = sale
    propertyData = Property.objects.all()
    data["property"] = propertyData
    if request.method == "POST":
        fori = request.POST.get("lst-sale-or-rent")
        location = request.POST.get("lstcity")
        type = request.POST.get("lst-property-type")
        curr = request.POST.get("lst-currency")
        price = request.POST.get("lst-price")
        size = request.POST.get("lst-size")
        room = request.POST.get("lst-bed-rooms")
        newPrice = price.split("-")
        newSize = size.split("-")

        if newPrice[0] != "":
            if(newPrice[1] == "lt"):
                propertyData = Property.objects.filter(Price__lte=newPrice[0])
            elif(newPrice[1] == "rt"):
                propertyData = Property.objects.filter(Price__gte=newPrice[1])
            else:
                propertyData = Property.objects.filter(
                    Price__gte=newPrice[0]).filter(Price__lte=newPrice[1])

        if newSize[0] != "":
            if(newSize[1] == "lt"):
                propertyData = Property.objects.filter(Size__lte=newSize[0])
            elif(newSize[1] == "rt"):
                propertyData = Property.objects.filter(Size__gte=newSize[0])
            else:
                propertyData = Property.objects.filter(
                    Size__gte=newSize[0]).filter(Price__lte=newSize[1])

        if(room != ""):
            propertyData = Property.objects.filter(Rooms=room)

        for i in propertyData:
            if((fori != "" and fori == i.Type) or (location != "" and location.lower() == i.Location.lower()) or (type != "" and type == i.PropertyType) or (curr != "" and curr == i.Currency)):
                newList.append(i)
        data["property"] = newList

    return render(request, "property.html", data)


@login_required(login_url="/login")
def addProperty(request):
    if(not request.user.userdetails.verified):
        return redirect("/property")
    form = propertyForm(request.POST or None, request.FILES or None)
    message = None
    success = False
    if request.method == "POST":
        if form.is_valid():
            sale = form.cleaned_data.get("sale")
            furnished = form.cleaned_data.get("furnished")
            title = form.cleaned_data.get("title")
            desc = form.cleaned_data.get("description")
            location = form.cleaned_data.get("location")
            address = form.cleaned_data.get("address")
            type = form.cleaned_data.get("propertyType")
            currency = form.cleaned_data.get("currency")
            size = form.cleaned_data.get("size")
            price = form.cleaned_data.get("price")
            condition = form.cleaned_data.get("priceCondition")
            deposit = form.cleaned_data.get("deposit")
            agent = form.cleaned_data.get("agent")
            build = form.cleaned_data.get("build")
            room = form.cleaned_data.get("room")
            garage = form.cleaned_data.get("garage")
            bathroom = form.cleaned_data.get("bathroom")
            carspace = form.cleaned_data.get("carspace")
            indoor = request.POST.getlist("indoor")
            outdoor = request.POST.getlist("outdoor")
            echo = request.POST.getlist("echo")
            other = request.POST.getlist("other")
            image = form.cleaned_data.get("image")
            image1 = request.FILES.getlist("image1")
            subcat = form.cleaned_data.get("subcategory1")
            subcat1 = form.cleaned_data.get("subcategory2")
            subcat2 = form.cleaned_data.get("subcategory3")
            subcat3 = form.cleaned_data.get("subcategory4")
            subcat4 = form.cleaned_data.get("subcategpry5")
            try:
                data = Property.objects.update_or_create(user=request.user, Type=sale, Title=title, Description=desc, PropertyType=type,
                                                     Location=location, Address=address,
                                                     Size=size, Currency=currency, Price=price,
                                                     PriceConditions=condition, Deposit=deposit, AgentCommision=agent, BuildYear=build,
                                                     Rooms=room, Garages=garage, Bathroom=bathroom, CarSpaces=carspace,
                                                     FullyFurnished=furnished, IndoorFeaturs=indoor, OutdoorFeatures=outdoor,
                                                     EcoFeatures=echo, OtherFeatures=other, image1=image)
                if subcat != "":
                    Property.objects.update(id=data[0],SubCategory=subcat)
                elif(subcat1 != ""):
                    Property.objects.update(id=data[0],SubCategory=subcat1)
                elif(subcat2 != ""):
                    Property.objects.update(id=data[0],SubCategory=subcat2)
                elif(subcat3 != ""):
                    Property.objects.update(id=data[0],SubCategory=subcat3)
                elif(subcat4 != ""):
                    Property.objects.update(id=data[0],SubCategory=subcat4)

                for i in image1:
                    PropertyIMage.objects.update_or_create(
                    projectName=data[0], image=i)
                message = "Property Details Submitted"
                success = True
                return redirect("/property")

            except:
                message = "Something error happened"
                success =False
            
        else:
            success = False
            message = "Please Provide all details that is required Correctly"

    return render(request, "addProperty.html", {"form": form, "message": message, "success": success})


def propertyView(request, id):
    message = None
    success = False
    form = contact(request.POST or None)
    data = {}
    property = Property.objects.filter(id=id)
    imageData = PropertyIMage.objects.filter(projectName=property[0])
    data["property"] = property
    data["images"] = imageData
    data["id"] = id
    data["form"] = form
   
    if request.method == "POST" and request.user.username !="":
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            phone = form.cleaned_data.get("phone")
            messages = form.cleaned_data.get("message")
            Contact.objects.update_or_create(name=name,email=email,phone=phone,message=messages)
            subject = f"New Message by {request.user}"
            messageBody = "Message Body "+"\n"+"Name: "+name+"\n"+"Email: "+email+"\n"+"Phone: "+ phone+ "\n" +"Message "+ "\n"+messages
            try:
                send_mail(subject,messageBody,host_email,[host_email],fail_silently=False,auth_user=host_email,auth_password=host_password)
                message = "Messages Sended Successfully"
                success = True
                return redirect("/property")
            except:
                message = "Smtp server not setup properly"
                success =False
        else:
            message = "Please fill up the form correctly"
    data["message"] = message
    data["success"] = success
    return render(request, "propertyView.html", data)


def editProperty(request,id):
    imageList = []
    data = {}
    message = None
    success = False
    propertyData = Property.objects.filter(id=id)
    imageData = PropertyIMage.objects.filter(projectName=propertyData[0])
    imageLength = imageData.count()
    data["length"] = imageLength
    if(propertyData[0].user != request.user):
        return redirect("/property")

    data["data"] = propertyData
    for i in imageData:
        name = str(i.image)
        imageList.append(name)
    data["imageData"] = imageList
    form = propertyForm(request.POST or None, request.FILES or None)
    data["form"]  = form

    if request.method == "POST":
        if form.is_valid():
            sale = form.cleaned_data.get("sale")
            furnished = form.cleaned_data.get("furnished")
            title = form.cleaned_data.get("title")
            desc = form.cleaned_data.get("description")
            location = form.cleaned_data.get("location")
            address = form.cleaned_data.get("address")
            type = form.cleaned_data.get("propertyType")
            currency = form.cleaned_data.get("currency")
            size = form.cleaned_data.get("size")
            price = form.cleaned_data.get("price")
            condition = form.cleaned_data.get("priceCondition")
            deposit = form.cleaned_data.get("deposit")
            agent = form.cleaned_data.get("agent")
            build = form.cleaned_data.get("build")
            room = form.cleaned_data.get("room")
            garage = form.cleaned_data.get("garage")
            bathroom = form.cleaned_data.get("bathroom")
            carspace = form.cleaned_data.get("carspace")
            indoor = request.POST.getlist("indoor")
            outdoor = request.POST.getlist("outdoor")
            echo = request.POST.getlist("echo")
            other = request.POST.getlist("other")
            image = form.cleaned_data.get("image")
            image1 = request.FILES.getlist("image1")
            subcat = form.cleaned_data.get("subcategory1")
            subcat1 = form.cleaned_data.get("subcategory2")
            subcat2 = form.cleaned_data.get("subcategory3")
            subcat3 = form.cleaned_data.get("subcategory4")
            subcat4 = form.cleaned_data.get("subcategpry5")
            try:
                propertyData.update(Type=sale, Title=title, Description=desc, PropertyType=type,
                                                     Location=location, Address=address,
                                                     Size=size, Currency=currency, Price=price,
                                                     PriceConditions=condition, Deposit=deposit, AgentCommision=agent, BuildYear=build,
                                                     Rooms=room, Garages=garage, Bathroom=bathroom, CarSpaces=carspace,
                                                     FullyFurnished=furnished, IndoorFeaturs=indoor, OutdoorFeatures=outdoor,
                                                     EcoFeatures=echo, OtherFeatures=other)
                

                if(image):
                    test = Property(user=request.user,id=id, Type=sale, Title=title, Description=desc, PropertyType=type,
                                                     Location=location, Address=address,
                                                     Size=size, Currency=currency, Price=price,
                                                     PriceConditions=condition, Deposit=deposit, AgentCommision=agent, BuildYear=build,
                                                     Rooms=room, Garages=garage, Bathroom=bathroom, CarSpaces=carspace,
                                                     FullyFurnished=furnished, IndoorFeaturs=indoor, OutdoorFeatures=outdoor,
                                                     EcoFeatures=echo, OtherFeatures=other,image1=image)
                    test.save()
                
                if subcat != "":
                    propertyData.update(SubCategory=subcat)
                elif(subcat1 != ""):
                    propertyData.update(SubCategory=subcat1)
                elif(subcat2 != ""):
                    propertyData.update(SubCategory=subcat2)
                elif(subcat3 != ""):
                    propertyData.update(SubCategory=subcat3)
                elif(subcat4 != ""):
                    propertyData.update(SubCategory=subcat4)

                if(image1):
                    imageData.delete()
                    for i in image1:
                        PropertyIMage.objects.update_or_create(projectName=propertyData[0],image=i)
                        
                message = "Property Details Updated"
                success = True

            except Exception as e:
                message = "Something error happened"
                success =False
        else:
            success = False
            message = "Please Provide all details that is required Correctly"

    data["message"] = message
    data["success"] = success
    return render(request,"editProperty.html",data)


def structure(request):
    data = {}
    data["currency"] = currency
    data["ptype"] = pType
    newList = []
    structureData = models.Structure.objects.all()
    data["structure"] = structureData
    if request.method == "POST":
        location = request.POST.get("lstcity")
        type = request.POST.get("lst-property-type")
        curr = request.POST.get("lst-currency")
        price = request.POST.get("lst-price")
        size = request.POST.get("lst-size")
        room = request.POST.get("lst-bed-rooms")
        newPrice = price.split("-")
        newSize = size.split("-")

        if newPrice[0] != "":
            if(newPrice[1] == "lt"):
                structureData = models.Structure.objects.filter(
                    Price__lte=newPrice[0])
            elif(newPrice[1] == "rt"):
                structureData = models.Structure.objects.filter(
                    Price__gte=newPrice[1])
            else:
                structureData = models.Structure.objects.filter(
                    Price__gte=newPrice[0]).filter(Price__lte=newPrice[1])

        if newSize[0] != "":
            if(newSize[1] == "lt"):
                structureData = models.Structure.objects.filter(
                    Size__lte=newSize[0])
            elif(newSize[1] == "rt"):
                structureData = models.Structure.objects.filter(
                    Size__gte=newSize[0])
            else:
                structureData = models.Structure.objects.filter(
                    Size__gte=newSize[0]).filter(Price__lte=newSize[1])

        if(room != ""):
            structureData = models.Structure.objects.filter(Rooms=room)

        for i in structureData:
            if((type != "" and type == i.PropertyType) or (location != "" and location.lower() == i.Location.lower()) or (curr != "" and curr in i.Currency)):
                newList.append(i)
        data["structure"] = newList
    return render(request, "structure.html", data)


@login_required(login_url="/login")
def addStructure(request):
    if(not request.user.userdetails.verified):
        return redirect("/structure")
    message = None
    success = False
    form = forms2.Structure(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            currency = form.cleaned_data.get("currency")
            type = form.cleaned_data.get("propertyType")
            category = form.cleaned_data.get("category")
            desc = form.cleaned_data.get("description")
            location = form.cleaned_data.get("location")
            address = form.cleaned_data.get("address")
            size = form.cleaned_data.get("size")
            price = form.cleaned_data.get("price")
            room = form.cleaned_data.get("room")
            final = form.cleaned_data.get("final")
            middle = form.cleaned_data.get("middle")
            initial = form.cleaned_data.get("initial")
            image1 = form.cleaned_data.get("image")
            image2 = request.FILES.getlist("image1")
            try:
                data = models.Structure.objects.update_or_create(user=request.user, PropertyType=type, Category=category,
                                                             Description=desc, Currency=currency, Location=location, Address=address, Size=size, Price=price,
                                                             Rooms=room, FinalCost=final, MiddleCost=middle, InitialCost=initial, image1=image1)
                for i in image2:
                    StructureImage.objects.update_or_create(
                    projectName=data[0], image=i)
                message = "Property Details Submitted"
                success = True
                return redirect("/structure")
            except:
                message = "Something error happened"
                success =False
                
        else:
            success = False
            message = "Please Provide all details that is required Correctly"

    return render(request, "addStructure.html", {"form": form, "message": message, "success": success})


def structureView(request, id):
    message = None
    success= False
    form = contact(request.POST or None)
    data = {}
    structure = models.Structure.objects.filter(id=id)
    imageData = StructureImage.objects.filter(projectName=structure[0])
    data["structure"] = structure
    data["images"] = imageData
    data["id"] = id
    data["form"] = form
    if request.method == "POST" and request.user.username != "":
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            phone = form.cleaned_data.get("phone")
            messages = form.cleaned_data.get("message")
            Contact.objects.update_or_create(name=name,email=email,phone=phone,message=messages)
            subject = f"New Message by {request.user}"
            messageBody = "Message Body "+"\n"+"Name: "+name+"\n"+"Email: "+email+"\n"+"Phone: "+ phone+ "\n" +"Message "+ "\n"+messages
            try:
                send_mail(subject,messageBody,host_email,[host_email],fail_silently=False,auth_user=host_email,auth_password=host_password)
                message = "Messages Sended Successfully"
                success = True
                return redirect("/structure")
            except:
                message = "Smtp server not setup properly"
                success =False
        else:
            message = "Please fill up the form correctly"

    data["message"] = message
    data["success"] = success
    return render(request, "structureView.html", data)


def editStructure(request,id):
    imageList = []
    data = {}
    message = None
    success = False
    propertyData = models.Structure.objects.filter(id=id)
    imageData = StructureImage.objects.filter(projectName=propertyData[0])
    imageLength = imageData.count()
    data["length"] = imageLength
    if(propertyData[0].user != request.user):
        return redirect("/structure")

    data["data"] = propertyData
    for i in imageData:
        name = str(i.image)
        imageList.append(name)
    data["imageData"] = imageList
    form = forms2.Structure(request.POST or None, request.FILES or None)
    data["form"]  = form

    if request.method == "POST":
        if form.is_valid():
            currency = form.cleaned_data.get("currency")
            type = form.cleaned_data.get("propertyType")
            category = form.cleaned_data.get("category")
            desc = form.cleaned_data.get("description")
            location = form.cleaned_data.get("location")
            address = form.cleaned_data.get("address")
            size = form.cleaned_data.get("size")
            price = form.cleaned_data.get("price")
            room = form.cleaned_data.get("room")
            final = form.cleaned_data.get("final")
            middle = form.cleaned_data.get("middle")
            initial = form.cleaned_data.get("initial")
            image1 = form.cleaned_data.get("image")
            image2 = request.FILES.getlist("image1")
            try:
                propertyData.update(PropertyType=type, Category=category,
                                                             Description=desc, Currency=currency, Location=location, Address=address, Size=size, Price=price,
                                                             Rooms=room, FinalCost=final, MiddleCost=middle, InitialCost=initial)
                if(image1):
                    test = models.Structure(user=request.user,id=id, PropertyType=type, Category=category,
                                                             Description=desc, Currency=currency, Location=location, Address=address, Size=size, Price=price,
                                                             Rooms=room, FinalCost=final, MiddleCost=middle, InitialCost=initial,image1=image1)
                    test.save()
                
                if(image2):
                    imageData.delete()
                    for i in image2:
                        StructureImage.objects.update_or_create(projectName=propertyData[0],image=i)

                message = "Structure Details Updated"
                success = True
            except:
                message = "Something error happened"
                success =False
                
        else:
            success = False
            message = "Please Provide all details that is required Correctly"

    data["message"] = message
    data["success"] = success
    return render(request,"editStructure.html",data)


def equipment(request):
    data = {}
    data["currency"] = currency
    data["ptype"] = models.Equipment.type
    data["fori"] = models.Equipment.hire
    newList = []
    equipmentData = models.Equipment.objects.all()
    data["equipment"] = equipmentData
    if request.method == "POST":
        location = request.POST.get("lstcity")
        type = request.POST.get("lst-property-type")
        curr = request.POST.get("lst-currency")
        price = request.POST.get("lst-price")
        fori = request.POST.get("lst-sale-or-rent")
        newPrice = price.split("-")

        if newPrice[0] != "":
            if(newPrice[1] == "lt"):
                equipmentData = models.Equipment.objects.filter(
                    Price__lte=newPrice[0])
            elif(newPrice[1] == "rt"):
                equipmentData = models.Equipment.objects.filter(
                    Price__gte=newPrice[1])
            else:
                equipmentData = models.Equipment.objects.filter(
                    Price__gte=newPrice[0]).filter(Price__lte=newPrice[1])

        for i in equipmentData:
            if((location != "" and location.lower() == i.Location.lower()) or (type != "" and type == i.EquipmentType) or (curr != "" and curr == i.Currency) or (fori != "" and fori == i.Hire)):
                newList.append(i)
        data["equipment"] = newList

    return render(request, "equipments.html", data)


@login_required(login_url="/login")
def addEquipment(request):
    if(not request.user.userdetails.verified):
        return redirect("/equipment")
    form = forms2.Equipment(request.POST or None, request.FILES or None)
    message = None
    success = False
    if request.method == "POST":
        if form.is_valid():
            desc = form.cleaned_data.get("description")
            location = form.cleaned_data.get("location")
            address = form.cleaned_data.get("address")
            price = form.cleaned_data.get("price")
            type = form.cleaned_data.get("equipmentType")
            currency = form.cleaned_data.get("currency")
            hire = form.cleaned_data.get("hire")
            status = form.cleaned_data.get("status")
            image1 = form.cleaned_data.get("image")
            image2 = request.FILES.getlist("image1")
            try:

                data = models.Equipment.objects.update_or_create(user=request.user, Description=desc, Location=location,
                                                             Address=address, Price=price, EquipmentType=type, Currency=currency, Hire=hire, Status=status, image1=image1)
                for i in image2:
                    EquipmentImage.objects.update_or_create(
                    projectName=data[0], image=i)
                message = "Property Details Submitted"
                success = True
                return redirect("/equipment")
            except:
                message = "Something error happened"
                success =False
           
        else:
            success = False
            message = "Please Provide all details that is required Correctly"

    return render(request, "addEquipment.html", {"form": form, "message": message, "success": success})


def equipmentView(request, id):
    message = None
    success = False
    form = contact(request.POST or None)
    data = {}
    equipment = models.Equipment.objects.filter(id=id)
    imageData = EquipmentImage.objects.filter(projectName=equipment[0])
    data["equipment"] = equipment
    data["images"] = imageData
    data["id"] = id
    data["form"] = form
    if request.method == "POST" and request.user.username != "":
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            phone = form.cleaned_data.get("phone")
            messages = form.cleaned_data.get("message")
            Contact.objects.update_or_create(name=name,email=email,phone=phone,message=messages)
            subject = f"New Message by {request.user}"
            messageBody = "Message Body "+"\n"+"Name: "+name+"\n"+"Email: "+email+"\n"+"Phone: "+ phone+ "\n" +"Message "+ "\n"+messages
            try:
                send_mail(subject,messageBody,host_email,[host_email],fail_silently=False,auth_user=host_email,auth_password=host_password)
                message = "Messages Sended Successfully"
                success = True
                return redirect("/equipment")
            except:
                message = "Smtp server not setup properly"
                success =False
        else:
            message = "Please fill up the form correctly"
    data["message"] = message
    data["success"] = success
    return render(request, "equipmentView.html", data)


def services(request):
    data = {}
    newList = []
    data["ptype"] = models.Service.serviceType
    data["currency"] = currency
    serviceData = models.Service.objects.all()
    data["service"] = serviceData

    if request.method == "POST":
        location = request.POST.get("lstcity")
        type = request.POST.get("lst-property-type")
        curr = request.POST.get("lst-currency")

        for i in serviceData:
            if((type != "" and type == i.ServiceType) or (location != "" and location.lower() == i.Location.lower()) or (curr != "" and curr == i.Currency)):
                newList.append(i)
        data["service"] = newList

    return render(request, "services.html", data)

@login_required(login_url="/login")
def addService(request):
    if(not request.user.userdetails.verified):
        return redirect("/services")
    message = None
    success = False
    form = forms2.Service(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            title = form.cleaned_data.get("title")
            desc = form.cleaned_data.get("description")
            location = form.cleaned_data.get("location")
            address = form.cleaned_data.get("address")
            price = form.cleaned_data.get("price")
            currency = form.cleaned_data.get("currency")
            type = form.cleaned_data.get("type")
            image1 = form.cleaned_data.get("image")
            image2 = request.FILES.getlist("image1")
            try:
                data = models.Service.objects.update_or_create(user=request.user, Title=title, Description=desc,
                                                           Location=location, Address=address, Price=price, Currency=currency, ServiceType=type, image1=image1)
                for i in image2:
                    ServiceImage.objects.update_or_create(
                    projectName=data[0], image=i)
                message = "Property Details Submitted"
                success = True
                return redirect("/services")
            except:
                message = "Something error happened"
                success =False
            
        else:
            success = False
            message = "Please Provide all details that is required Correctly"

    return render(request, "addService.html", {"form": form, "message": message, "success": success})


def serviceView(request, id):
    message = None
    success = False
    form = contact(request.POST or None)
    data = {}
    service = models.Service.objects.filter(id=id)
    imageData = ServiceImage.objects.filter(projectName=service[0])
    data["service"] = service
    data["images"] = imageData
    data["id"] = id
    data["form"] = form
    if request.method == "POST" and request.user.username != "":
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            phone = form.cleaned_data.get("phone")
            messages = form.cleaned_data.get("message")
            Contact.objects.update_or_create(name=name,email=email,phone=phone,message=messages)
            subject = f"New Message by {request.user}"
            messageBody = "Message Body "+"\n"+"Name: "+name+"\n"+"Email: "+email+"\n"+"Phone: "+ phone+ "\n" +"Message "+ "\n"+messages
            try:
                send_mail(subject,messageBody,host_email,[host_email],fail_silently=False,auth_user=host_email,auth_password=host_password)
                message = "Messages Sended Successfully"
                success = True
                return redirect("/services")
            except:
                message = "Smtp server not setup properly"
                success =False
        else:
            message = "Please fill up the form correctly"

    data["message"] = message
    data["success"] = success
    return render(request, "serviceView.html", data)



def editService(request,id):
    imageList = []
    data = {}
    message = None
    success = False
    propertyData = models.Service.objects.filter(id=id)
    imageData = ServiceImage.objects.filter(projectName=propertyData[0])
    imageLength = imageData.count()
    data["length"] = imageLength
    if(propertyData[0].user != request.user):
        return redirect("/services")

    data["data"] = propertyData
    for i in imageData:
        name = str(i.image)
        imageList.append(name)
    data["imageData"] = imageList
    form = forms2.Service(request.POST or None, request.FILES or None)
    data["form"]  = form

    if request.method == "POST":
        if form.is_valid():
            title = form.cleaned_data.get("title")
            desc = form.cleaned_data.get("description")
            location = form.cleaned_data.get("location")
            address = form.cleaned_data.get("address")
            price = form.cleaned_data.get("price")
            currency = form.cleaned_data.get("currency")
            type = form.cleaned_data.get("type")
            image1 = form.cleaned_data.get("image")
            image2 = request.FILES.getlist("image1")
            try:
                propertyData.update(Title=title, Description=desc,
                                                           Location=location, Address=address, Price=price, Currency=currency, ServiceType=type)
                
                if(image1):
                    test = models.Service(id=id,image1=image1,Price=price,user=request.user,Title=title,Description=desc,Location=location,Address=address,Currency=currency,ServiceType=type)
                    test.save()
                
                if(image2):
                    imageData.delete()
                    for i in image2:
                        ServiceImage.objects.update_or_create(projectName=propertyData[0],image=i)

                
                message = "Service Details Updated"
                success = True
            except:
                message = "Something error happened"
                success =False
            
        else:
            success = False
            message = "Please Provide all details that is required Correctly"

    data["message"] = message
    data["success"] = success

    return render(request,"editService.html",data)


def material(request):
    data = {}
    newList = []
    data["ptype"] = models.Material.type
    data["currency"] = currency
    materialData = models.Material.objects.all()
    data["material"] = materialData

    if request.method == "POST":
        type = request.POST.get("lst-property-type")
        curr = request.POST.get("lst-currency")
        price = request.POST.get("lst-price")
        newPrice = price.split("-")

        if newPrice[0] != "":
            if(newPrice[1] == "lt"):
                materialData = models.Material.objects.filter(
                    Price__lte=newPrice[0])
            elif(newPrice[1] == "rt"):
                materialData = models.Material.objects.filter(
                    Price__gte=newPrice[1])
            else:
                materialData = models.Material.objects.filter(
                    Price__gte=newPrice[0]).filter(Price__lte=newPrice[1])

        for i in materialData:
            if((type != "" and type == i.Category) or (curr != "" and curr == i.Currency)):
                newList.append(i)
        data["material"] = newList
    return render(request, "materials.html", data)


@login_required(login_url="/login")
def addMaterial(request):
    if(not request.user.userdetails.verified):
        return redirect("/materials")
    message = None
    success = False
    form = forms2.Material(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            title = form.cleaned_data.get("title")
            item = form.cleaned_data.get("item")
            desc = form.cleaned_data.get("description")
            address = form.cleaned_data.get("address")
            quantity = form.cleaned_data.get("quantity")
            price = form.cleaned_data.get("price")
            category = form.cleaned_data.get("category")
            currency = form.cleaned_data.get("currency")
            weight = form.cleaned_data.get("weight")
            image1 = form.cleaned_data.get("image")
            image2 = request.FILES.getlist("image1")
            try:
                data = models.Material.objects.update_or_create(user=request.user, Item=item, Title=title,
                                                            Description=desc, Address=address, Quantity=quantity, Price=price, Category=category, Currency=currency, Weight=weight, image1=image1)
                for i in image2:
                    MaterialImage.objects.update_or_create(
                        projectName=data[0], image=i)
                message = "Property Details Submitted"
                success = True
                return redirect("/materials")
            except:
                message = "Something error happened"
                success =False
            
        else:
            success = False
            message = "Please Provide all details that is required Correctly"

    return render(request, "addMaterial.html", {"form": form, "message": message, "success": success})


def materialView(request, id):
    message = None
    success  = False
    form = contact(request.POST or None)
    data = {}
    material = models.Material.objects.filter(id=id)
    imageData = MaterialImage.objects.filter(projectName=material[0])
    data["material"] = material
    data["images"] = imageData
    data["id"] = id
    data["form"] = form
    
    if request.method == "POST" and request.user.username != "":
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            phone = form.cleaned_data.get("phone")
            messages = form.cleaned_data.get("message")
            Contact.objects.update_or_create(name=name,email=email,phone=phone,message=messages)
            subject = f"New Message by {request.user}"
            messageBody = "Message Body "+"\n"+"Name: "+name+"\n"+"Email: "+email+"\n"+"Phone: "+ phone+ "\n" +"Message "+ "\n"+messages
            try:
                send_mail(subject,messageBody,host_email,[host_email],fail_silently=False,auth_user=host_email,auth_password=host_password)
                message = "Messages Sended Successfully"
                success = True
                return redirect("/materials")
            except:
                message = "Smtp server not setup properly"
                success =False
        else:
            message = "Please fill up the form correctly"

    data["message"] = message
    data["success"] = success
    return render(request, "materialView.html", data)


def editMaterial(request,id):
    imageList = []
    data = {}
    message = None
    success = False
    propertyData = models.Material.objects.filter(id=id)
    imageData = MaterialImage.objects.filter(projectName=propertyData[0])
    imageLength = imageData.count()
    data["length"] = imageLength
    if(propertyData[0].user != request.user):
        return redirect("/materials")

    data["data"] = propertyData
    for i in imageData:
        name = str(i.image)
        imageList.append(name)
    data["imageData"] = imageList
    form = forms2.Material(request.POST or None, request.FILES or None)
    data["form"]  = form

    if request.method == "POST":
        if form.is_valid():
            title = form.cleaned_data.get("title")
            item = form.cleaned_data.get("item")
            desc = form.cleaned_data.get("description")
            address = form.cleaned_data.get("address")
            quantity = form.cleaned_data.get("quantity")
            price = form.cleaned_data.get("price")
            category = form.cleaned_data.get("category")
            currency = form.cleaned_data.get("currency")
            weight = form.cleaned_data.get("weight")
            image1 = form.cleaned_data.get("image")
            image2 = request.FILES.getlist("image1")
            try:
                propertyData.update(Item=item, Title=title,
                                                            Description=desc, Address=address, Quantity=quantity, Price=price, Category=category, Currency=currency, Weight=weight)
               
                if(image1):
                    test =  models.Material(user=request.user,id=id,Item=item, Title=title,
                                                            Description=desc, Address=address, Quantity=quantity, Price=price, Category=category, Currency=currency, Weight=weight,image1=image1)
                    test.save()
                
                if(image2):
                    imageData.delete()
                    for i in image2:
                        MaterialImage.objects.update_or_create(projectName=propertyData[0],image=i)

                message = "Material Details updated"
                success = True
            except:
                message = "Something error happened"
                success =False
            
        else:
            success = False
            message = "Please Provide all details that is required Correctly"

    data["message"] = message
    data["success"] = success
    return render(request,"editMaterial.html",data)


def flats(request):
    data = {}
    newList = []
    data["currency"] = currency
    flatData = models.Flat.objects.all()
    data["flat"] = flatData
    data["ptype"] = models.Flat.gender
    data["term"] = models.Flat.termChoice
    data["occu"] = models.Flat.occupation
    if request.method == "POST":
        sale = request.POST.get("sale")
        location = request.POST.get("lst-city")
        room = request.POST.get("lst-bed-rooms")
        curr = request.POST.get("lst-currency")
        price = request.POST.get("rent")
        price1 = request.POST.get("rent1")
        gender = request.POST.get("gender")
        term = request.POST.get("term")
        bill = request.POST.get("bill")
        short = request.POST.get("short")
        toilet = request.POST.get("toilet")
        furnish = request.POST.get("furnish")
        park = request.POST.get("park")
        garage = request.POST.get("garage")
        garden = request.POST.get("garden")
        balcony = request.POST.get("balcony")
        living = request.POST.get("living")
        broadband = request.POST.get("broadband")
        age = request.POST.get("age")
        occupation = request.POST.get("occu")
        gender = request.POST.get("gender")
        smoker = request.POST.get("smoker")
        pets = request.POST.get("pet")

        for i in flatData:
            if((sale != "" and sale == i.Type) or (curr != "" and curr == i.Currency) or (location != "" and location.lower() == i.Location.lower()) or (price != "" and int(price) >= i.Price) or (price1 != "" and int(price1) <= i.Price)
               or (room != "" and room == i.Rooms) or (gender != "" and gender == i.Gender) or (term != "" and term == i.Term) or (bill != "" and bill == i.Bills) or (short != "" and short == i.Short) or (toilet != "" and toilet == i.Toilet)
               or (furnish != "" and furnish == i.Furnishing) or (park != "" and park == i.Parking) or (garage != "" and garage == i.Garage) or (garden != "" and garden == i.Garden) or (balcony != "" and balcony == i.Balcony) or (living != "" and living == i.LivingRoom)
               or (broadband != "" and broadband == i.Broadband) or (age != "" and age == i.MaxAge) or (occupation != "" and occupation == i.Occupation) or (smoker != "" and smoker == i.Smoker) or (pets != "" and pets == i.Pets)):
                newList.append(i)
        data["flat"] = newList
    return render(request, "flats.html", data)



@login_required(login_url="/login")
def addFlat(request):
    if(not request.user.userdetails.verified):
        return redirect("/flats")
    message = None
    success = False
    form = Flatform(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            title = form.cleaned_data.get("title")
            sale = form.cleaned_data.get("sale")
            location = form.cleaned_data.get("location")
            description = form.cleaned_data.get("description")
            address = form.cleaned_data.get("address")
            room = form.cleaned_data.get("room")
            price = form.cleaned_data.get("price")
            bills = form.cleaned_data.get("bills")
            term = form.cleaned_data.get("term")
            short = form.cleaned_data.get("short")
            toilet = form.cleaned_data.get("toilet")
            furnish = form.cleaned_data.get("furnishing")
            park = form.cleaned_data.get("parking")
            garage = form.cleaned_data.get("garage")
            garden = form.cleaned_data.get("garden")
            living = form.cleaned_data.get("living")
            balcony = form.cleaned_data.get("balcony")
            broadband = form.cleaned_data.get("broadband")
            age = form.cleaned_data.get("age")
            occupation = form.cleaned_data.get("occupation")
            gender = form.cleaned_data.get("gender")
            smoker = form.cleaned_data.get("smoker")
            pets = form.cleaned_data.get("pets")
            currency = form.cleaned_data.get("currency")
            image = form.cleaned_data.get("image")
            image1 = form.cleaned_data.get("image1")
            try:
                data = Flat.objects.update_or_create(user=request.user, Type=sale, Title=title, Description=description, Address=address, Rooms=room,
                                                 Price=price, Bills=bills, Term=term, Short=short, Toilet=toilet, Furnishing=furnish, Parking=park, Garage=garage, Balcony=balcony, LivingRoom=living,
                                                 Broadband=broadband, MaxAge=age, Gender=gender, Occupation=occupation, Smoker=smoker, Pets=pets, Garden=garden, Location=location, Currency=currency, image1=image)
                return redirect("/flats")
            except:
                message = "Something error happened"
                success =False

            for i in image1:
                FlatImage.objects.update_or_create(
                    projectName=data[0], image=i)
            message = "Property Details Submitted"
            success = True
            return redirect("/flats")
        else:
            message = "Please fill out the form correctly"
            success = False
    return render(request, "addFlat.html", {"form": form, "message": message, "success": success})


def flatView(request, id):
    message = None
    success = False
    form = contact(request.POST or None)
    data = {}
    flat = models.Flat.objects.filter(id=id)
    imageData = FlatImage.objects.filter(projectName=flat[0])
    data["flat"] = flat
    data["images"] = imageData
    data["id"] = id
    data["form"] = form
    
    if request.method == "POST" and request.user.username !="":
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            phone = form.cleaned_data.get("phone")
            messages = form.cleaned_data.get("message")
            Contact.objects.update_or_create(name=name,email=email,phone=phone,message=messages)
            subject = f"New Message by {request.user}"
            messageBody = "Message Body "+"\n"+"Name: "+name+"\n"+"Email: "+email+"\n"+"Phone: "+ phone+ "\n" +"Message "+ "\n"+messages
            try:
                send_mail(subject,messageBody,host_email,[host_email],fail_silently=False,auth_user=host_email,auth_password=host_password)
                message = "Messages Sended Successfully"
                success = True
                return redirect("/flats")
            except:
                message = "Smtp server not setup properly"
                success =False
        else:
            message = "Please fill up the form correctly"
    data["message"] = message
    data["success"] = success
    return render(request, "flatView.html", data)


@login_required(login_url="/login")
def logou(request):
    logout(request)
    return redirect("/login")
