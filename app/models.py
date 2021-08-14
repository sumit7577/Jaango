from django.db import  models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone

phone_regex = RegexValidator(regex=r'^\+1?\d{9,15}$', message="Phone number must be entered in the format: '+(country Code)99999'. Up to 18 digits allowed.")
# Create your models here.

state = [
    ("Abia","Abia"),
    ("Adamawa","Adamawa"),
    ("Akwa Ibom","Akwa Ibom"),
    ("Anambra","Anambra"),
    ("Bauchi","Bauchi"),
    ("Bayelsa","Bayelsa"),
    ("Benue","Benue"),
    ("Borno","Borno"),
    ("Cross River","Cross River"),
    ("Delta","Delta"),
    ("Ebonyi","Ebonyi"),
    ("Edo","Edo"),
    ("Ekiti","Ekiti"),
    ("Enugu","Enugu"),
    ("Federal Capital Territory","Federal Capital Territory"),
    ("Gombe","Gombe"),
    ("Imo","Imo"),
    ("Jigawa","Jigawa"),
    ("kaduna","kaduna"),
    ("Kano","Kano"),
    ("Katsina","Katsina"),
    ("Kebbi","Kebbi"),
    ("Kogi","Kogi"),
    ("Kwara","Kwara"),
    ("Lagos","Lagos"),
    ("Nasarawa","Nasarawa"),
    ("Niger","Niger"),
    ("Ogun","Ogun"),
    ("Ondo","Ondo"),
    ("Osun","Osun"),
    ("Oyo","Oyo"),
    ("Plateau","Plateau"),
    ("Rivers","Rivers"),
    ("Sokoto","Sokoto"),
    ("Taraba","Taraba"),
    ("Yobe","Yobe"),
    ("Zamfara","Zamfara")
]


class UserDetails(models.Model):
    UserChoice = [
        ("Company","Company"),
        ("Individual","Individual")
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.CharField(validators=[phone_regex],max_length=18)
    userType = models.CharField(max_length=20,default="",choices=UserChoice)
    Latitude = models.FloatField(null=True,blank=True)
    Longitude =  models.FloatField(null=True,blank=True)
    verified = models.BooleanField(blank=True,null=True)

    def __str__(self) -> str:
        return self.user.username



class Files(models.Model):
    userName = models.ForeignKey(User,on_delete=models.CASCADE)
    files = models.FileField(upload_to="documents",blank=True)

    def __str__(self):
        return self.userName.username



class Property(models.Model):
    propertyChoices = [
        ("Concrete Structure","Concrete Structure"),
        ("Steel Structure","Steel Structure"),
        ("Home Stay","Home Stay"),
        ("Land","Land"),
        ("Flat","Flat"),
        ("House","House")
    ]
    subCategory = [
        ("Flat/House/Apartment","Flat/House/Apartment"),
        ("Trees Work","Trees Work"),
        ("Gardening","Gardening"),
        ("Public","Public"),
        ("Private","Private"),
        ("In Dispute","In Dispute"),
        ("Farm Land","Farm Land"),
        ("Non-Cultivated","Non-Cultivated"),
        ("Cultivated","Cultivated"),
        ("Partially Furnished","Partially Furnished"),
        ("Fully Furnished","Fully Furnished"),

    ]

    subCategory1 = [
        ("Flat/House/Apartment","Flat/House/Apartment")
    ]

    subCategory2 = [
        ("Trees Work","Trees Work"),
        ("Gardening","Gardening"),
    ]

    subCategory3 = [
        ("Public","Public"),
        ("Private","Private"),
    ]

    subCategory4 = [
       ("In Dispute","In Dispute"),
        ("Farm Land","Farm Land"),
        ("Non-Cultivated","Non-Cultivated"),
        ("Cultivated","Cultivated"),
    ]

    subCategory5 = [
       ("Partially Furnished","Partially Furnished"),
        ("Fully Furnished","Fully Furnished"),
    ]
    currency = [
        ("₦ NGN","₦ NGN"),
        ("$ USD","$ USD"),
        ("£ GBP","£ GBP"),
        ("€ EUR","€ EUR"),
    ]

    type= [
        ("Sale","Sale"),
        ("Rent","Rent")
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Type = models.CharField(max_length=20,choices=type)
    Title= models.CharField(default="",max_length=50)
    Description = models.CharField(default="",max_length=250)
    PropertyType = models.CharField(choices=propertyChoices,default="",max_length=50)
    SubCategory = models.CharField(default="",choices=subCategory,max_length=50)
    Location= models.CharField(default="",max_length=150)
    Address = models.CharField(default="",max_length=200)
    Size = models.IntegerField(default=0)
    Currency= models.CharField(default="",choices=currency,max_length=20)
    Price = models.IntegerField()
    PriceConditions = models.CharField(default="",max_length=150,null=True,blank=True)
    Deposit = models.IntegerField(null=True,blank=True)
    AgentCommision = models.IntegerField(null=True,blank=True)
    BuildYear = models.IntegerField(null=True,blank=True)
    Rooms = models.IntegerField(null=True,blank=True)
    Garages = models.IntegerField(null=True,blank=True)
    Bathroom = models.IntegerField(null=True,blank=True)
    CarSpaces = models.IntegerField(null=True,blank=True)
    FullyFurnished = models.BooleanField(blank=True,null=True)
    IndoorFeaturs = models.CharField(max_length=500,null=True,blank=True)
    OutdoorFeatures = models.CharField(max_length=500,null=True,blank=True)
    EcoFeatures = models.CharField(max_length=500,null=True,blank=True)
    OtherFeatures = models.CharField(max_length=500,null=True,blank=True)
    Date = models.DateField(default=timezone.now)
    image1 = models.FileField(upload_to="Images",null=True,blank=True)
    image1Verify = models.BooleanField(blank=True,null=True)

    def __str__(self) -> str:
        return self.Title

class PropertyIMage(models.Model):
    projectName = models.ForeignKey(Property,on_delete=models.CASCADE)
    image = models.FileField(upload_to="Images",null=True,blank=True)
    Verified = models.BooleanField(null=True,blank=True)


    def __str__(self) -> str:
        return self.projectName.Title


class Equipment(models.Model):
    type =[("Tractor","Tractor"),("JCB","JCB"),("Cutter","Cutter"),("TTT","TTT")]
    hire = [("Hire","Hire"),("Buy","Buy")]
    status = [("New","New"),("Used","Used")]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Description = models.CharField(default="",max_length=250)
    Location= models.CharField(default="",max_length=150)
    Address = models.CharField(default="",max_length=200)
    Price = models.IntegerField()
    EquipmentType = models.CharField(max_length=50,choices=type)
    Currency= models.CharField(choices=Property.currency,max_length=20)
    Hire = models.CharField(choices=hire,max_length=30)
    Status = models.CharField(choices=status,max_length=30)
    Date = models.DateField(default=timezone.now)
    image1 = models.FileField(upload_to="Images",null=True,blank=True)
    image1Verify = models.BooleanField(blank=True,null=True)

    def __str__(self) -> str:
        return self.user.username


class EquipmentImage(models.Model):
    projectName = models.ForeignKey(Equipment,on_delete=models.CASCADE)
    image = models.FileField(upload_to="Images",null=True,blank=True)
    Verified = models.BooleanField(null=True,blank=True)


    def __str__(self) -> str:
        return self.projectName.EquipmentType


class Structure(models.Model):
    category = [("Commercial","Commercial"),("Residential","Residential")]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    PropertyType = models.CharField(max_length=50,choices=Property.propertyChoices)
    Category = models.CharField(max_length=30,choices=category)
    Currency= models.CharField(choices=Property.currency,max_length=20)
    Description = models.CharField(default="",max_length=250)
    Location= models.CharField(default="",max_length=150)
    Address = models.CharField(default="",max_length=200)
    Size = models.IntegerField()
    Price = models.IntegerField()
    Rooms = models.IntegerField()
    FinalCost = models.IntegerField()
    MiddleCost = models.IntegerField()
    InitialCost = models.IntegerField()
    Date = models.DateField(default=timezone.now)
    image1 = models.FileField(upload_to="Images",null=True,blank=True)
    image1Verify = models.BooleanField(blank=True,null=True)
    

    def __str__(self) -> str:
        return self.user.username


class StructureImage(models.Model):
    projectName = models.ForeignKey(Structure,on_delete=models.CASCADE)
    image = models.FileField(upload_to="Images",null=True,blank=True)
    Verified = models.BooleanField(null=True,blank=True)


    def __str__(self) -> str:
        return self.projectName.PropertyType

    

class Service(models.Model):
    serviceType = [
        ("Electrician","Electrician"),
        ("Architecture","Architecture"),
        ("Event management1","Event management1"),
        ("new category for testing T5231","new category for testing T5231"),
        ("Adminstration..","Adminstration.."),
        ("Supervision","Supervision"),
        ("Plumbing","Plumbing")
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Title= models.CharField(default="",max_length=50)
    Description = models.CharField(default="",max_length=250)
    Location= models.CharField(default="",max_length=150)
    Address = models.CharField(default="",max_length=200)
    Price = models.IntegerField()
    Currency= models.CharField(choices=Property.currency,max_length=20)
    ServiceType = models.CharField(choices=serviceType,max_length=80)
    Date = models.DateField(default=timezone.now)
    image1 = models.FileField(upload_to="Images",null=True,blank=True)
    image1Verify = models.BooleanField(blank=True,null=True)
    


    def __str__(self) -> str:
        return self.Title

class ServiceImage(models.Model):
    projectName = models.ForeignKey(Service,on_delete=models.CASCADE)
    image = models.FileField(upload_to="Images",null=True,blank=True)
    Verified = models.BooleanField(null=True,blank=True)


    def __str__(self) -> str:
        return self.projectName.Title


class Material(models.Model):
    type = [
        ("Test Cate","Test Cate"),
        ("Cement","Cement"),
        ("Tiles","Tiles"),
        ("Sand","Sand"),
        ("Gravel","Gravel"),
        ("Iron","Iron"),
        ("Limestone","Limestone"),
    ]
    weight = [
        ("KG","KG"),
        ("Pound","Pound"),
        ("Tonne","Tonne"),
        ("Grams","Grams"),
        ("Milligrams","Milligrams"),
        ("Meters","Meters"),
        ("Square Meters","Square Meters"),
        ("Centimeters","Centimeters"),
        ("Inches","Inches"),
        ("Millimeters","Millimeters")
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Item= models.CharField(default="",max_length=20)
    Title= models.CharField(default="",max_length=50)
    Description = models.CharField(default="",max_length=250)
    Address = models.CharField(default="",max_length=200)
    Quantity = models.IntegerField()
    Price = models.IntegerField()
    Category = models.CharField(max_length=50,choices=type)
    Currency= models.CharField(choices=Property.currency,max_length=20)
    Weight = models.CharField(choices=weight,max_length=80)
    Date = models.DateField(default=timezone.now)
    image1 = models.FileField(upload_to="Images",null=True,blank=True)
    image1Verify = models.BooleanField(blank=True,null=True)
    

    def __str__(self) -> str:
        return self.Title


class MaterialImage(models.Model):
    projectName = models.ForeignKey(Material,on_delete=models.CASCADE)
    image = models.FileField(upload_to="Images",null=True,blank=True)
    Verified = models.BooleanField(null=True,blank=True)


    def __str__(self) -> str:
        return self.projectName.Title


class Flat(models.Model):
    termChoice = [
        ("1 Month","1 Month"),
        ("2 Months","2 Months"),
        ("3 Months","3 Months"),
        ("4 Months","4 Months"),
        ("5 Months","5 Months"),
        ("6 Months","6 Months"),
        ("7 Months","7 Months"),
        ("8 Months","8 Months"),
        ("9 Months","9 Months"),
        ("10 Months","10 Months"),
        ("11 Months","11 Months"),
        ("1 Year","1 Year"),
        ("1.5 Years","1.5 Years"),
        ("2 Years","2 Years"),
        ("2+ Year","2+ Year")
    ]
    occupation = [
        ("Students","Students"),
        ("Professionals","Professionals")
    ]
    gender = [
        ("Couple","Couple"),
        ("Male","Male"),
        ("Either Male or Female","Either Male or Female"),
        ("Female","Female")
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Type = models.CharField(max_length=20,choices=Property.type)
    Title= models.CharField(default="",max_length=50)
    Location= models.CharField(default="",max_length=150)
    Description = models.CharField(default="",max_length=250)
    Address = models.CharField(default="",max_length=200)
    Rooms = models.IntegerField()
    Price = models.IntegerField()
    Currency= models.CharField(choices=Property.currency,max_length=20)
    Bills = models.BooleanField(default=0)
    Term = models.CharField(max_length=90,choices=termChoice)
    Short = models.BooleanField()
    Toilet = models.BooleanField()
    Furnishing = models.BooleanField()
    Parking = models.BooleanField()
    Garage = models.BooleanField()
    Garden = models.BooleanField()
    Balcony = models.BooleanField()
    LivingRoom = models.BooleanField()
    Broadband = models.BooleanField()
    MaxAge = models.IntegerField()
    Gender = models.CharField(max_length=50,choices=gender)
    Occupation = models.CharField(max_length=40,choices =occupation)
    Smoker = models.BooleanField()
    Pets = models.BooleanField()
    Date = models.DateField(default=timezone.now)
    image1 = models.FileField(upload_to="Images",null=True,blank=True)
    image1Verify = models.BooleanField(blank=True,null=True)
    

    def __str__(self):
        return self.Title


class FlatImage(models.Model):
    projectName = models.ForeignKey(Flat,on_delete=models.CASCADE)
    image = models.FileField(upload_to="Images",null=True,blank=True)
    Verified = models.BooleanField(null=True,blank=True)


    def __str__(self) -> str:
        return self.projectName.Title


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=80)
    phone = models.CharField(max_length=25,null=True,blank=True)
    message = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

class SMTP(models.Model):
    email = models.CharField(max_length=100,null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self) -> str:
        return self.email