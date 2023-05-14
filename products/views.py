from django.shortcuts import render,redirect
from products.models import Products,Customer_info,Email
from products.forms import *
import json

def index(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        data=Email(email=email)
        data.save() 
        return redirect('/contactus')   
    return render(request, 'index.html', {'pro' : Products.objects.all()})

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

def conditions(request):
    return render(request,'conditions_general.html' , {'conditions':'conditions'})

def contact(request):
    return   render(request,'contact_us.html',{'contact':'contact'})

def private(request):
    return render(request,'private_policy.html',{'private':'private'}) 



    