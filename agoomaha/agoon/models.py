from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,blank=True,null=True)
    email = models.CharField(max_length=200,blank=True,null=True)
    username = models.CharField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=200,blank=True,null=True)
    profile_image = models.ImageField(default="profile1.jpeg", null=True, blank=True)
    phone = models.CharField(max_length=200,blank=True,null=True)
    created =  models.DateField(auto_now_add=True)
  


    def __str__(self):
        return str(self.user.username)

class Order(models.Model):
    Owner = models.ForeignKey(Customer,null=True,blank=True,on_delete=models.SET_NULL)
    name = models.CharField('Student Name', max_length=180)
    age = models.IntegerField('student age')
    place_birth = models.CharField('place of birth', max_length=180)
    gender = models.CharField('gender', max_length=80)
    clases = models.CharField('class', max_length=60)
    school = models.CharField('school', max_length=90, null=True)
    image =models.ImageField(default="profile1.jpeg", null=True, blank=True)
    parent_name = models.CharField('parent Name', max_length=180)
    phone_number = models.CharField('contact phone', max_length=60)
    account_number = models.CharField('acoount number', max_length=60)
    parent_image =models.ImageField(default="profile1.jpeg", null=True, blank=True)
    phone = models.CharField('Student Name', max_length=180,null=True,blank=True)


    def __str__(self):
        return self.name



class StudentReport(models.Model):
    name = models.CharField('Student name', null=True, max_length=200)
    school_name = models.CharField('school name', null=True, max_length=200)
    head_teacher = models.CharField('Head Teacher name', null=True, max_length=200)
    yearly = models.CharField(null=True, max_length=20)
    Refrence = models.CharField('reference letter number',null=True,blank=True, max_length=80)
    date = models.DateTimeField(auto_now_add=True)
    IRE_Mid = models.CharField('Mid Term IRE Marks', max_length=20, null=True,blank=True)
    Arabic_Mid = models.CharField('Mid Term Arabic Marks', max_length=20, null=True,blank=True)
    Somali_Mid = models.CharField('Mid Term Somali Marks', max_length=20, null=True,blank=True)
    English_Mid = models.CharField('Mid Term English Marks', max_length=20, null=True,blank=True)
    Math_Mid = models.CharField('Mid Term Math Marks', max_length=20, null=True,blank=True)
    Physics_Mid = models.CharField('Mid Term Physics Marks', max_length=20, null=True,blank=True)
    Chemistry_Mid = models.CharField('Mid Term Chemistry Marks', max_length=20, null=True,blank=True)
    Biology_Mid = models.CharField('Mid Term Biology Marks', max_length=20, null=True,blank=True)
    Geogrphy_Mid = models.CharField('Mid Term Geogrphy Marks', max_length=20, null=True,blank=True)
    History_Mid = models.CharField('Mid Term History Marks', max_length=20, null=True,blank=True)
    ICT_Mid = models.CharField('Mid Term ICT Marks', max_length=20, null=True,blank=True)
    Business_Mid = models.CharField('Mid Term Business Marks', max_length=20, null=True,blank=True)
    Total_Mid = models.CharField('MidTerm Total Marks', max_length=20, null=True,blank=True)
    IRE = models.CharField('Final IRE Marks', max_length=20, null=True,blank=True)
    Arabic = models.CharField('Final Arabic Marks', max_length=20, null=True,blank=True)
    Somali = models.CharField('Final Somali Marks', max_length=20, null=True,blank=True)
    English = models.CharField('Final English Marks', max_length=20, null=True,blank=True)
    Math = models.CharField('Final Math Marks', max_length=20, null=True,blank=True)
    Physics = models.CharField('Final Physics Marks', max_length=20, null=True,blank=True)
    Chemistry = models.CharField('Final Chemistry Marks', max_length=20, null=True,blank=True)
    Biology = models.CharField('Final Biology Marks', max_length=20, null=True,blank=True)
    Geogrphy = models.CharField('Final Geogrphy Marks', max_length=20, null=True,blank=True)
    History = models.CharField('Final History Marks', max_length=20, null=True,blank=True)
    ICT = models.CharField('Final ICT Marks', max_length=20, null=True,blank=True)
    Business = models.CharField('Final Business Marks', max_length=20, null=True,blank=True)
    Total = models.CharField('Total Marks', max_length=20, null=True,blank=True)
    Quran = models.CharField('Quran ', max_length=20, null=True,blank=True)
   
    


    def __str__(self):
        return self.name


