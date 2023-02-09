from django import forms

from crud.models import Vehicle,User
from django.core.validators import RegexValidator



class VehicleUpdateForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        fields=['vehicle_number', 'vehicle_type','vehicle_model','vehicle_description']
        widgets={
            "vehicle_number":forms.TextInput(attrs={'class':'form-control','placeholder':'vehicle number'}),
            "vehicle_type":forms.Select(attrs={'class':'form-select'}),
            "vehicle_model":forms.TextInput(attrs={'class':'form-control',"Placeholder":"vehicle model"}),
            "vehicle_description":forms.TextInput(attrs={'class':'form-control','placeholder':'About vehicle'})
             
        }


class vehiclecreateform(forms.ModelForm):

    class Meta:
        model=Vehicle
        fields = ['vehicle_number', 'vehicle_type', 'vehicle_model', 'vehicle_description']

        widgets={
            "vehicle_number":forms.TextInput(attrs={'class':'form-control','placeholder':'vehicle number'}),
            "vehicle_type":forms.Select(attrs={'class':'form-select'}),
            "vehicle_model":forms.TextInput(attrs={'class':'form-control',"Placeholder":"vehicle model"}),
            "vehicle_description":forms.TextInput(attrs={'class':'form-control','placeholder':'About vehicle'})
             
        }



class RegistrationForm(forms.ModelForm):    #same as serializer
    
    class Meta:
        model=User
        fields=['username','email','password','role']
        widgets={
            "username":forms.TextInput(attrs={'class':'form-control text-info',"Placeholder":"username"}),
            "email":forms.EmailInput(attrs={'class':'form-control',"Placeholder":"Email"}),
            "password":forms.PasswordInput(attrs={'class':'form-control',"Placeholder":"password"}),
            "role":forms.Select(attrs={'class':'form-select'})
             
        }




class LoginForm(forms.Form):               #login il data onnum save avanilla, so 'Form' kodutha mathi 
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","Placeholder":"username"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","Placeholder":"password"}))
