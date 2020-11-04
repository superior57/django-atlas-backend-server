from django.shortcuts import render
from django.http import HttpResponse

from lswebapi.models import ProductDetails
from lswebapi.models import UserDetails
import requests
import json
import datetime
from django.shortcuts import redirect

def deleteuser(request):
	if request.GET:
		uid = request.GET['id']
	else:
		return HttpResponse("<B>Missing User ID</B>")
	
	
	UserDetails.objects.filter(user_id=uid).delete()
			
	return redirect('/')

def edituser(request):
	if request.GET:
		uid = request.GET['id']

	elif request.POST:
		uid = request.POST['user_id']
		firstname = request.POST['first_name']
		lastname  = request.POST['last_name']
		phone     = request.POST['phone']
		#UserDetails.objects.filter(pk=uid).update( first_name=firstname, last_name=lastname, phone=phone)

		user = UserDetails.objects.get(user_id=uid)
		user.first_name = firstname
		user.last_name  = lastname
		user.phone	= phone
		user.save()

		return redirect('/list')
	else:
		return HttpResponse("<B>Missing User ID</B>")

	user = UserDetails.objects.get(pk=uid);

	return render(request,"edituser.html", {'user':user});		

def adduser(request):
	#print(request.POST);
	#Check if data is posted or not 
	if  request.POST:
		#Get posted values
		firstname = request.POST['first_name']		
		lastname  = request.POST['last_name']
		phone     = request.POST['phone']
		
		#check if user with this phone and name already exists in the database
		if( UserDetails.objects.filter(first_name=firstname, last_name=lastname, phone=phone).exists() ):
			print ("User already exists with the phone number : " + phone)
			return HttpResponse("User already exists...")
		else:		
			#Add user to the database
			ud = UserDetails.objects.create(first_name=firstname, last_name=lastname, phone=phone, date_added=datetime.date.today())
			print (ud.user_id)

	return render(request, "adduser.html", {} )

def home(request):	
	return render(request, "home.html", {} )

def list(request):
	users = UserDetails.objects.all()
	return render(request, 'list.html', {'users':users})

