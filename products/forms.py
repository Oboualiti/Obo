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
            }),
            'city':forms.TextInput(attrs={
            "placeholder":"ادخل المدينة",
            "class":"form-control",
            }),
            'number':forms.NumberInput(attrs={
            "placeholder":"ادخل رقم الهاتف",
            "class":"form-control",
            }),
            
                }