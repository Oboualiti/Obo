from django.shortcuts import render,redirect
from products.models import Products,Customer_info,Email,Customer_infobycart
from products.forms import *
import json

def index(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        data=Email(email=email)
        data.save() 
        return redirect('/done_email')   
    return render(request, 'index.html', {'pro' : Products.objects.all()})


def doneemail(request):
    return render(request, 'done_email.html')


def done(request):
    return render(request, 'done_demande.html', {'done':'done'})

def product_detial(request , id):
    product_detail=Products.objects.get(id=id)
    customer = CustomerForm()
    if request.method == 'POST':
        quantity=request.POST.get('quantity')
        full_name=request.POST.get('full_name')
        city=request.POST.get('city')
        number=request.POST.get('number')
       
        myid = request.POST.get('id')
        id_customer=Customer_info(myid=myid,quantity=quantity,full_name=full_name,city=city,number=number)
        
        id_customer.save()
        return redirect('/done')
        
    return render(request, 'products_details.html',{'prod':product_detail,'customer':customer , 'pro':Products.objects.all()})

def shoes(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        data=Email(email=email)
        data.save() 
        return redirect('/done_email') 
    return render(request,'shoes.html' , {'pro':Products.objects.all()})

def tshirt(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        data=Email(email=email)
        data.save() 
        return redirect('/done_email') 
    return   render(request,'tshirt.html',{'pro':Products.objects.all()})

def pants(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        data=Email(email=email)
        data.save() 
        return redirect('/done_email') 
    return render(request,'pants.html',{'pro':Products.objects.all()}) 


def product_detialbycart(request):
    customerbycart = CustomerbycartForm()
    if request.method == 'POST':
        full_name=request.POST.get('full_name')
        city=request.POST.get('city')
        number=request.POST.get('number')
        myid = request.POST.get('myid')
        somme=request.POST.get('somme')
        id_customerbycart=Customer_infobycart(myid=myid,full_name=full_name,city=city,number=number,somme=somme)
        
        id_customerbycart.save()
        return redirect('/done')
        
    return render(request, 'cartinfo.html',{ 'customerbycart':customerbycart ,'pro':Products.objects.all()})

def productcart(request):
    
    return render(request,'productcart.html',{'pro':Products.objects.all()})     