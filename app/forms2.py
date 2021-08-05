from django import forms
from django.forms.fields import Field
from .models import Property,Equipment,Structure,Service,Material,Flat

Outdoor = [
    ("Carport","Carport"),
    ("Garage","Garage"),
    ("Open Car Spaces","Open Car Spaces"),
    ("Remote Garage","Remote Garage"),
    ("Secure Parking","Secure Parking"),
    ("Swimming Pool","Swimming Pool"),
    ("Tennis Court","Tennis Court"),
    ("Balcony","Balcony"),
    ("Deck","Deck"),
    ("Courtyard","Courtyard"),
    ("Outdoor Entertaining Area","Outdoor Entertaining Area"),
    ("Fully Fenced","Fully Fenced"),
    ("24Hr Security","24Hr Security")
]

Indoor = [
    ("Alarm System","Alarm System"),
    ("Intercom","Intercom"),
    ("Ensuite","Ensuite"),
    ("Dishwasher","Dishwasher"),
    ("Built-in wardrobes","Built-in wardrobes"),
    ("Ducted Vacuum System","Ducted Vacuum System"),
    ("Gym","Gym"),
    ("Indoor Spa","Indoor Spa"),
    ("Floorboards","Floorboards"),
    ("Broadband Internet","Broadband Internet"),
    ("PayTV Access","PayTV Access"),
    ("Fireplace","Fireplace"),
    ("Ducted Heating","Ducted Heating"),
    ("Split-system Heating","Split-system Heating"),
    ("Hydronic Heating","Hydronic Heating"),
    ("Gas Heating","Gas Heating"),
    ("Ducted Cooling","Ducted Cooling"),
    ("Air Conditioning","Air Conditioning"),
    ("Lift","Lift"),
    ("Running Water","Running Water"),
    ("Washing Machine","Washing Machine")
]

Echo = [
    ("Solar Panels","Solar Panels"),
    ("Solar Hot Water","Solar Hot Water"),
    ("Water Tank","Water Tank"),
    ("Grey Water System","Grey Water System"),
    ("Energy efficiency rating -High","Energy efficiency rating -High"),
    ("Energy efficiency rating -Medium","Energy efficiency rating -Medium"),
    ("Energy efficiency rating -Low","Energy efficiency rating -Low")
]

Other = [
    ("Pets Allowed","Pets Allowed"),
    ("Disability Features","Disability Features"),
    ("Waterfront","Waterfront"),
    ("Water View","Water View"),
    ("Ocean View","Ocean View"),
    ("River View","River View"),
    ("Hill/Mountain View","Hill/Mountain View"),
    ("Development Projects","Development Projects"),
    ("ERCAAN Association","ERCAAN Association"),
]

class propertyForm(forms.Form):
    sale = forms.ChoiceField(required=True,choices=[("Sale","For Sale"),("Rent","For Rent")],
    widget=forms.RadioSelect(
         attrs={
                "class":"validation"
            }
    ))

    furnished = forms.ChoiceField(required=True,choices=[("True","Yes"),("False","No")],
    widget=forms.Select(
         attrs={
                "class":"validation"
            }
    ))

    title = forms.CharField(required=True,min_length=5,max_length=20,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Title",
                "class":"validation"
            }
        ))
    
    description = forms.CharField(required=True,min_length=20,max_length=250,
        widget=forms.Textarea(
            attrs={
                "rows":4,
                "class":"validation"
            }
        ))

    location = forms.CharField(required=True,min_length=10,max_length=150,
        widget=forms.TextInput(
            attrs={
                "class":"validation"
            }
        ))

    address = forms.CharField(required=True,min_length=20,max_length=200,
        widget=forms.Textarea(
            attrs={
                "rows":4,
                "class":"validation"
            }
        ))

    propertyType = forms.ChoiceField(required=True,choices=Property.propertyChoices,
        widget=forms.Select(
            attrs={
                "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
        ))

    currency = forms.ChoiceField(required=True,choices=Property.currency,
        widget=forms.Select(
            attrs={
                "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
        ))

    size = forms.IntegerField(required=True,
        widget=forms.NumberInput(
            attrs={
                "class":"validation",
                "placeholder":"in SQ.FT"
            }
        ))

    price = forms.IntegerField(required=True,
        widget=forms.NumberInput(
            attrs={
                "class":"validation"
            }
        ))

    priceCondition = forms.CharField(min_length=8,max_length=150,
        widget=forms.TextInput(
            attrs={
                "class":"validation"
            }
        ))

    deposit = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class":"validation"
            }
        ))

    agent = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class":"validation"
            }
        ))
    
    build = forms.IntegerField(required=True,
        widget=forms.NumberInput(
            attrs={
                "class":"validation"
            }
        ))

    room = forms.IntegerField(required=True,
        widget=forms.NumberInput(
            attrs={
                "class":"validation"
            }
        ))

    garage = forms.IntegerField(required=True,
        widget=forms.NumberInput(
            attrs={
                "class":"validation"
            }
        ))

    bathroom = forms.IntegerField(required=True,
        widget=forms.NumberInput(
            attrs={
                "class":"validation"
            }
        ))

    carspace = forms.IntegerField(required=True,
        widget=forms.NumberInput(
            attrs={
                "class":"validation"
            }
        ))

    image = forms.ImageField(required=True,
        widget=forms.FileInput(
            attrs={
                "class":"validation"
            }
        ))

    image1 = forms.ImageField(required=True,
        widget=forms.FileInput(
            attrs={
                "class":"validation"
            }
        ))
    
    indoor = forms.ChoiceField(choices=Outdoor,required=True,
        widget = forms.CheckboxSelectMultiple(
            attrs={
                "class":"validation"
            }
        )
    )

    outdoor = forms.ChoiceField(choices=Indoor,required=True,
        widget = forms.CheckboxSelectMultiple(
            attrs={
                "class":"validation"
            }
        )
    )

    echo = forms.ChoiceField(choices=Echo,required=True,
        widget = forms.CheckboxSelectMultiple(
            attrs={
                "class":"validation"
            }
        )
    )

    other = forms.ChoiceField(choices=Other,required=True,
        widget = forms.CheckboxSelectMultiple(
            attrs={
                "class":"validation"
            }
        )
    )

    
class Structure(forms.Form):
    currency = forms.ChoiceField(required=True,choices=Property.currency,
        widget=forms.Select(
            attrs={
                "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
        ))
    
    propertyType = forms.ChoiceField(required=True,choices=Property.propertyChoices,
        widget=forms.Select(
            attrs={
                "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
        ))

    category = forms.ChoiceField(required=True,choices=Structure.category,
        widget=forms.Select(
            attrs={
                "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
        ))

    image = forms.ImageField(required=True,
        widget=forms.FileInput(
            attrs={
                "class":"validation"
            }
        ))

    image1 = forms.ImageField(required=True,
        widget=forms.FileInput(
            attrs={
                "class":"validation"
            }
        ))


    description = forms.CharField(required=True,min_length=20,
        widget=forms.Textarea(
            attrs={
                "rows":4,
                "class":"validation"
            }
        ))

    location = forms.CharField(required=True,min_length=10,
        widget=forms.TextInput(
            attrs={
                "class":"validation"
            }
        ))

    address = forms.CharField(required=True,min_length=20,
        widget=forms.Textarea(
            attrs={
                "rows":4,
                "class":"validation"
            }
        ))

    size = forms.IntegerField(required=True,
        widget=forms.NumberInput(
            attrs={
                "class":"validation",
                "placeholder":"in SQ.FT"
            }
        ))

    price = forms.IntegerField(required=True,
        widget=forms.NumberInput(
            attrs={
                "class":"validation"
            }
        ))

    room = forms.IntegerField(required=True,
        widget=forms.NumberInput(
            attrs={
                "class":"validation"
            }
        ))

    final = forms.IntegerField(required=True,
        widget=forms.NumberInput(
            attrs={
                "class":"validation"
            }
        ))

    middle = forms.IntegerField(required=True,
        widget=forms.NumberInput(
            attrs={
                "class":"validation"
            }
        ))

    initial = forms.IntegerField(required=True,
        widget=forms.NumberInput(
            attrs={
                "class":"validation"
            }
        ))


class Equipment(forms.Form):
    image = forms.ImageField(required=True,
        widget=forms.FileInput(
            attrs={
                "class":"validation"
            }
        ))

    image1 = forms.ImageField(required=True,
        widget=forms.FileInput(
            attrs={
                "class":"validation"
            }
        ))


    description = forms.CharField(required=True,min_length=20,max_length=250,
        widget=forms.Textarea(
            attrs={
                "rows":4,
                "class":"validation"
            }
        ))

    location = forms.CharField(required=True,min_length=10,max_length=150,
        widget=forms.TextInput(
            attrs={
                "class":"validation"
            }
        ))

    address = forms.CharField(required=True,min_length=20,max_length=200,
        widget=forms.Textarea(
            attrs={
                "rows":4,
                "class":"validation"
            }
        ))

    price = forms.IntegerField(required=True,
        widget=forms.NumberInput(
            attrs={
                "class":"validation"
            }
        ))

    equipmentType = forms.ChoiceField(required=True,choices=Equipment.type,
        widget=forms.Select(
            attrs={
                "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
        ))

    currency = forms.ChoiceField(required=True,choices=Property.currency,
        widget=forms.Select(
            attrs={
                "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
        ))

    hire = forms.ChoiceField(required=True,choices=Equipment.hire,
        widget=forms.Select(
            attrs={
                "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
        ))

    status = forms.ChoiceField(required=True,choices=Equipment.status,
        widget=forms.Select(
            attrs={
                "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
        ))
    



class Service(forms.Form):
    image = forms.ImageField(required=True,
        widget=forms.FileInput(
            attrs={
                "class":"validation"
            }
        ))

    image1 = forms.ImageField(required=True,
        widget=forms.FileInput(
            attrs={
                "class":"validation"
            }
        ))

        
    title = forms.CharField(required=True,min_length=5,max_length=50,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Title",
                "class":"validation"
            }
        ))
    
    description = forms.CharField(required=True,min_length=20,max_length=250,
        widget=forms.Textarea(
            attrs={
                "rows":4,
                "class":"validation"
            }
        ))

    location = forms.CharField(required=True,min_length=10,max_length=150,
        widget=forms.TextInput(
            attrs={
                "class":"validation"
            }
        ))

    address = forms.CharField(required=True,min_length=20,max_length=200,
        widget=forms.Textarea(
            attrs={
                "rows":4,
                "class":"validation"
            }
        ))

    price = forms.IntegerField(required=True,
        widget=forms.NumberInput(
            attrs={
                "class":"validation"
            }
        ))

    currency = forms.ChoiceField(required=True,choices=Property.currency,
        widget=forms.Select(
            attrs={
                "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
        ))

    

    type = forms.ChoiceField(required=True,choices=Service.serviceType,
        widget=forms.Select(
            attrs={
                "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
        ))


class Material(forms.Form):
    image = forms.ImageField(required=True,
        widget=forms.FileInput(
            attrs={
                "class":"validation"
            }
        ))

    image1 = forms.ImageField(required=True,
        widget=forms.FileInput(
            attrs={
                "class":"validation"
            }
        ))
    

    item = forms.CharField(required=True,min_length=5,max_length=20,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Brand",
                "class":"validation"
            }
        ))


    title = forms.CharField(required=True,min_length=5,max_length=50,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Title",
                "class":"validation"
            }
        ))
    
    description = forms.CharField(required=True,min_length=20,max_length=250,
        widget=forms.Textarea(
            attrs={
                "rows":4,
                "class":"validation"
            }
        ))

    address = forms.CharField(required=True,min_length=20,max_length=200,
        widget=forms.Textarea(
            attrs={
                "rows":4,
                "class":"validation"
            }
        ))
    
    quantity = forms.IntegerField(required=True,
        widget=forms.NumberInput(
            attrs={
                "class":"validation"
            }
        ))

    price = forms.IntegerField(required=True,
        widget=forms.NumberInput(
            attrs={
                "class":"validation"
            }
        ))
    
    category = forms.ChoiceField(required=True,choices=Material.type,
        widget=forms.Select(
            attrs={
                "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
        ))
    
    currency = forms.ChoiceField(required=True,choices=Property.currency,
        widget=forms.Select(
            attrs={
                "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
        ))

    
    weight = forms.ChoiceField(required=True,choices=Material.weight,
        widget=forms.Select(
            attrs={
                "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
        ))


class Flatform(forms.Form):
    image = forms.ImageField(required=False,
        widget=forms.FileInput(
            attrs={
                "class":"validation"
            }
        ))

    image1 = forms.ImageField(required=False,
        widget=forms.FileInput(
            attrs={
                "class":"validation"
            }
        ))

    sale = forms.ChoiceField(required=False,choices=[("Sale","For Sale"),("Rent","For Rent")],
    widget=forms.RadioSelect(
         attrs={
                "class":"validation"
            }
    ))


    title = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Title",
                "class":"validation"
            }
        ))
        
    currency = forms.ChoiceField(required=False,choices=Property.currency,
        widget=forms.Select(
            attrs={
                "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
        ))
    
    location = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "class":"validation"
            }
        ))
    
    description = forms.CharField(required=False,
        widget=forms.Textarea(
            attrs={
                "rows":4,
                "class":"validation"
            }
        ))

    address = forms.CharField(required=False,
        widget=forms.Textarea(
            attrs={
                "rows":4,
                "class":"validation"
            }
        ))

    room = forms.IntegerField(required=False,
        widget=forms.NumberInput(
            attrs={
                "class":"validation",
                "placeholder":"Ex:1,2,5,10"
            }
        ))

    price = forms.IntegerField(required=False,
        widget=forms.NumberInput(
            attrs={
                "class":"validation"
            }
        ))
    
    bills = forms.ChoiceField(required=False,choices=[("True","Yes"),("False","No")],
    widget=forms.Select(
         attrs={
                 "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
    ))

    term = forms.ChoiceField(required=False,choices=Flat.termChoice,
    widget=forms.Select(
         attrs={
                 "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
    ))

    short = forms.ChoiceField(required=False,choices=[("True","Yes"),("False","No")],
    widget=forms.Select(
         attrs={
                 "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
    ))

    toilet = forms.ChoiceField(required=False,choices=[("True","Yes"),("False","No")],
    widget=forms.Select(
         attrs={
                 "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
    ))

    furnishing = forms.ChoiceField(required=False,choices=[("True","Yes"),("False","No")],
    widget=forms.Select(
         attrs={
                 "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
    ))

    parking = forms.ChoiceField(required=False,choices=[("True","Yes"),("False","No")],
    widget=forms.Select(
         attrs={
                 "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
    ))

    garage = forms.ChoiceField(required=False,choices=[("True","Yes"),("False","No")],
    widget=forms.Select(
         attrs={
                 "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
    ))

    garden = forms.ChoiceField(required=False,choices=[("True","Yes"),("False","No")],
    widget=forms.Select(
         attrs={
                 "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
    ))

    living = forms.ChoiceField(required=False,choices=[("True","Yes"),("False","No")],
    widget=forms.Select(
         attrs={
                 "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
    ))

    balcony = forms.ChoiceField(required=False,choices=[("True","Yes"),("False","No")],
    widget=forms.Select(
         attrs={
                 "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
    ))

    broadband = forms.ChoiceField(required=False,choices=[("True","Yes"),("False","No")],
    widget=forms.Select(
         attrs={
                 "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
    ))


    #preferenace for terants
    age = forms.IntegerField(required=False,
        widget=forms.NumberInput(
            attrs={
                "class":"validation"
            }
        ))
    
    occupation = forms.ChoiceField(required=False,choices=Flat.occupation,
    widget=forms.Select(
         attrs={
                 "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
    ))

    gender = forms.ChoiceField(required=False,choices=Flat.gender,
    widget=forms.Select(
         attrs={
                 "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
    ))

    smoker = forms.ChoiceField(required=False,choices=[("True","Yes"),("False","No")],
    widget=forms.Select(
         attrs={
                 "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
    ))

    pets = forms.ChoiceField(required=False,choices=[("True","Yes"),("False","No")],
    widget=forms.Select(
         attrs={
                 "class":"block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded-lg h-10 px-4 md:w-full",
            }
    ))
    

