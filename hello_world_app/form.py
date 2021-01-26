from django import forms
from .models import User,data
from django.core import validators


class StudentRegistration(forms.ModelForm):
    # class Meta:
    #     model = User
    #     fields = ['name','email', 'password']
    #     widgets = {
    #         'name': forms.TextInput(attrs={'class':'form-control'}),
    #         'email': forms.EmailInput(attrs={'class':'form-control'}),
    #         'password': forms.PasswordInput(attrs={'class':'form-control'}),
    #     }
    class Meta():
        model = data
        fields = ('name','brand_name','regular_price_value','offer_price_value','currency','classification_l1','classification_l2','classification_l3','classification_l4','image_url',)
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','value':'None','placeholder':'name'}),
            'brand_name': forms.TextInput(attrs={'class':'form-control','value':'None','placeholder':'brand_name'}),
            'regular_price_value': forms.TextInput(attrs={'class':'form-control','value':'None','placeholder':'regular_price_value'}),
            'offer_price_value': forms.TextInput(attrs={'class':'form-control','value':'None','placeholder':'offer_price_value'}),
            'currency': forms.TextInput(attrs={'class':'form-control','value':'None','placeholder':'currency'}),
            'classification_l1': forms.TextInput(attrs={'class':'form-control','value':'None','placeholder':'classification_l1'}),
            'classification_l2': forms.TextInput(attrs={'class':'form-control','value':'None','placeholder':'classification_l2'}),
            'classification_l3': forms.TextInput(attrs={'class':'form-control','value':'None','placeholder':'classification_l3'}),
            'classification_l4': forms.TextInput(attrs={'class':'form-control','value':'None','placeholder':'classification_l4'}),
            'image_url': forms.TextInput(attrs={'class':'form-control','value':'None','placeholder':'image_url'}),
        }
