from django.urls import path
from . import views

app_name='product'

urlpatterns=[
    path('',views.index, name='Home'),
    path('<int:id>',views.product_detial,name='products_details' ),
    path('done',views.done, name='done'),
    path('conditions_general/',views.conditions,name='conditions'),
    path('contactus/',views.contact,name='contact'),
    path('private_policy/',views.private,name='private')
]