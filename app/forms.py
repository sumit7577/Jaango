from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


phone_regex = RegexValidator(regex=r'^\+1?\d{9,15}$', message="Phone number must be entered in the format: '(+12)99999'. Up to 18 digits allowed.")
UserChoice = [
        ("Company","Company"),
        ("Individual","Individual")
    ]

def customMobileValidator(mobile):
    data = False
    data = User.objects.filter(userdetails__mobile=mobile).exists()
    
    if(data == True):
        raise forms.ValidationError("Mobile Number already Exists")


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
        
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(min_length=8,max_length=18,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    first_name = forms.CharField(min_length=4,max_length=12,
        widget=forms.TextInput(
            attrs={
                "placeholder": "First Name",
                "class": "form-control"
            }
        ))

    last_name = forms.CharField(min_length=4,max_length=12,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last Name",
                "class": "form-control"
            }
        ))

    userType = forms.ChoiceField(choices=UserChoice,
        widget=forms.Select(
            attrs={
                "class":"form-control",
                "id":"userType"
            }
    ))
    

    mobile = forms.CharField(validators=[phone_regex,customMobileValidator],
        widget=forms.TextInput(
            attrs={
                "placeholder":"Mobile Number with Country Code ex(+1)9999",
                "class":"form-control",
                "id":"mobile"
            }
        ))

    def mobileCheck(self):
        mobilenumber = self.cleaned_data.get("mobile")
        data = customMobileValidator(mobilenumber)



    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','first_name','last_name')
