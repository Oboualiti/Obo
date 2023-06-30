from django.forms import ModelForm
from products.models import *
from django import forms
from django.views import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer_info
        fields = ("quantity","full_name","city","number")
        widgets = {
            'quantity':forms.NumberInput(attrs={
            "placeholder":"ادخل الكمية المرغوبة",
            "class":"form-control",
            "required":True,
            }),
            'full_name':forms.TextInput(attrs={
            "placeholder":"ادخل اسم الكامل",
            "class":"form-control",
            "required":True,
            }),
            'city':forms.TextInput(attrs={
            "placeholder":"ادخل المدينة",
            "class":"form-control",
            "required":True,
            }),
            'number':forms.NumberInput(attrs={
            "placeholder":"ادخل رقم الهاتف",
            "class":"form-control",
            "required":True,
            }),
            
                }
        
class CustomerbycartForm(ModelForm):
    class Meta:
        model = Customer_infobycart
        fields = ("full_name","city","number")
        widgets = {
            'full_name':forms.TextInput(attrs={
            "onkeyup":"getids()",   
            "placeholder":"ادخل اسم الكامل",
            "class":"form-control",
            "required":True,
            }),
            'city':forms.TextInput(attrs={
            "placeholder":"ادخل المدينة",
            "onkeyup":"sommeup()", 
            "class":"form-control",
            "required":True,
            }),
            'number':forms.NumberInput(attrs={
            "placeholder":"ادخل رقم الهاتف",
            "class":"form-control",
            "required":True,
            }),
            
                }        