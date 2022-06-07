from django.urls import path
from . import views


urlpatterns = [
	#login registration logout
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),


    # admin and user
    path('', views.home, name="home"),
    path('user/', views.userPage, name="user-page"),
    path('account/', views.accountSettings, name="account"),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('girls/',views.girls_data, name='girls'),
    path('contact/', views.contact, name="contact"),




    #crud
    path('addStudent/',views.addStudent, name='addstudent'),
    path('update_student/<student_id>', views.update_student, name="update_student"),
    path('delete_student/<student_id>', views.delete_student, name="delete_student"),
    path('show_student/<student_id>', views.show_student, name="show_student"),



    #report
    path('report', views.Report, name="report"),
    path('update_report/<boysreport_id>', views.update_report, name="update_report"),
    path('show_boysreport/<boysreport_id>', views.show_boysreport, name="show_boysreport"),
    path('addreport/', views.add_report, name="add_report"),
    path('delete_report/<boysreport_id>', views.delete_report, name="delete_report"),
    
  


]