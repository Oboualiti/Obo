from django.urls import path
from . import views

app_name='product'

urlpatterns=[
    path('',views.index, name='Home'),
    path('<int:id>',views.product_detial,name='products_details' ),
    path('done_email/',views.doneemail, name='done_email'),
    path('done',views.done, name='done'),
    path('shoes/',views.shoes,name='shoes'),
    path('pants/',views.pants,name='pants'),
    path('tshirt/',views.tshirt,name='tshirt'),
    path('cartinfo/', views.product_detialbycart ,name='cartinfo'),
    path('productcart/',views.productcart , name='productcart'),
]