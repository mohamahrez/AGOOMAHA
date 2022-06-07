from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import Order, Customer, StudentReport
from . forms import OrderForm,CustomerForm, StudentReportForm, CreateUserForm

#login imports
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#end login imports



#end report imports



#loging registration views

@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            #Added username after video because of error returning customer name if not added
            Customer.objects.create(
                user=user,
                name=user.username,
                )

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')
        

    context = {'form':form}
    return render(request, 'agoon/register.html', context)

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'login.html', context)



def logoutUser(request):
    logout(request)
    return redirect('login')
#end loging registration views

# admin and user views
@login_required(login_url='login')
@admin_only
def home(request):
	orders = Order.objects.all()
	
	customers = Customer.objects.all()
	
	total_customers = customers.count()

	total_orders = orders.count()
	

	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders, 'total_customers':total_customers}

	return render(request, 'index.html', context)


@login_required(login_url='login')
def userPage(request):

	orders = request.user.customer.order_set.filter(gender = 'male').order_by('name')

	total_orders = orders.count()
	
	print('ORDERS:', orders)
	context = {'orders':orders, 'total_orders':total_orders}
	return render(request, 'agoon/profile.html', context)

@login_required(login_url='login')
def girls_data(request,):
    orders = request.user.customer.order_set.filter(gender = 'female').order_by('name')
    return render(request, 'Agoon/profile.html', {
        "orders": orders
    })

@login_required(login_url='login')
def contact(request,):
    contact = Order.objects.all()
    return render(request, 'Agoon/ContectUs.html', {
        "contact": contact
    })

@login_required(login_url='login')
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES,instance=customer)
        if form.is_valid():
            form.save()


    context = {'form':form}
    return render(request, 'agoon/account_settings.html', context)

# end admin and user views



#crud
@login_required(login_url='login')
def addStudent(request):
    submitted = False
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('addstudent')
    else:
        form = OrderForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request,'agoon/studetinfo_form.html', {'form':form, 'submitted':submitted
    
    
    })
@login_required(login_url='login')
def update_student(request, student_id):
    order = Order.objects.get(pk=student_id)
    form = OrderForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'agoon/studetinfo_form.html', {
        "order": order,
        "form": form
    })

@login_required(login_url='login')
def delete_student(request, student_id):
    order = Order.objects.get(pk=student_id)
    order.delete()
    return redirect('/')

@login_required(login_url='login')
def show_student(request, student_id):
    order = Order.objects.get(pk=student_id)
    return render(request, 'agoon/show_boys.html', {
        "order": order
    })

#end crud

#
@login_required(login_url='login')
def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	

	

	context = {'customer':customer, 'orders':orders}
	return render(request, 'agoon/users.html',context)


#report
@login_required(login_url='login')
def Report(request,):
    report = StudentReport.objects.all()
    return render(request, 'Agoon/boys_report.html', {
        "report": report
    })

def show_boysreport(request, boysreport_id):
    boyreport_show = StudentReport.objects.get(pk=boysreport_id)
    return render(request, 'Agoon/pdf_template.html', {
        "boyreport_show": boyreport_show
    })

@login_required(login_url='login')
def update_report(request, boysreport_id):
    report = StudentReport.objects.get(pk=boysreport_id)
    form = StudentReportForm(request.POST or None, instance=report)
    if form.is_valid():
        form.save()
        return redirect('report')

    return render(request, 'Agoon/studetinfo_form.html', {
        "report": report,
        "form": form
    }) 

@login_required(login_url='login')
def add_report(request):
    submitted = False
    if request.method == "POST":
        form = StudentReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('report')
    else:
        form = StudentReportForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request,'Agoon/add_student.html', {'form':form, 'submitted':submitted
    
    
    })


@login_required(login_url='login')
def delete_report(request, boysreport_id):
    report = StudentReport.objects.get(pk=boysreport_id)
    report.delete()
    return redirect('report')








