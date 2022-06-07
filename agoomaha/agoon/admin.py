from django.contrib import admin
from . models import Order, Customer, StudentReport
# Register your models here.

admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(StudentReport)