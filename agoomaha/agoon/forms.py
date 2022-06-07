from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django.forms import ModelForm, widgets
from django import forms
from .models import Order, Customer, StudentReport
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm






class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('Owner', 'name', 'age', 'place_birth', 'gender', 'clases', 'school', 'image', 'parent_name', 'phone_number', 'account_number', 'parent_image')



class StudentReportForm(ModelForm):
    class Meta:
        model = StudentReport
        fields = '__all__'




class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']