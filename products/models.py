from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    petitcontent = models.CharField(max_length=100)
    price = models.IntegerField()
    notprice=models.IntegerField()
    image=models.ImageField(null=True, blank=True ,upload_to='photo/%y/%m/%d')
    image1=models.ImageField(null=True, blank=True ,upload_to='photo/%y/%m/%d')
    image2=models.ImageField(null=True, blank=True, upload_to='photo/%y/%m/%d')
    image3=models.ImageField(null=True, blank=True,upload_to='photo/%y/%m/%d')
    image4=models.ImageField(null=True, blank=True,upload_to='photo/%y/%m/%d')
    image5=models.ImageField(null=True, blank=True,upload_to='photo/%y/%m/%d')

    def __str__(self):
       return self.name    
    
class Customer_info(models.Model):
      quantity = models.IntegerField(null=True,blank=True)
      full_name= models.CharField(max_length=30 ,null=True,blank=True)
      city = models.CharField(max_length=40 ,null=True,blank=True)
      number = models.IntegerField(null=True,blank=True)
      
      myid = models.IntegerField(null=True,blank=True)
      
      def __str__(self):
         return (self.full_name +' ' + self.city)

class Email(models.Model):
   email=models.CharField(max_length=50)
         