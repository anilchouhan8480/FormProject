from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.db import connection
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

myCursor = connection.cursor() 

# Create your views here.

def signup(request):
	ef = EmployeeForm()
	if request.method == "POST":
		f = request.POST['fname']
		l = request.POST['lname']
		un = request.POST['uname']
		e = request.POST['email']
		pw = request.POST['pwd']
		age = request.POST['age']
		sal = request.POST['salary']
		ad = request.POST['addresh']

		#print(nm,age,sal,ad)
		u = User(username=un, password=make_password(pw), first_name=f, last_name=l, email=e)
		u.save()

		e = Employee(name=f, age=age, salary=sal, addr=ad)
		e.save()
		return redirect('/appp2/login/')


	return render(request, "signup.html")   
	

def login_call(request):

	if request.method == "POST":
		h = request.POST['uname']
		i = request.POST['pwd']

		user = authenticate(username=h, password=i)	

		if user:
			login(request, user)

			return redirect('/')
		else:
			return redirect('/appp2/login/')
			
	return render(request, 'login.html')