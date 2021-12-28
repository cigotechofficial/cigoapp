from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from home.models import Newuserinfo
from twilio.rest import Client

def handleSignup(request):
	if request.method == 'POST':
		fname = request.POST['fname']
		username = request.POST['email']
		phone = request.POST['phone']
		pass1 = request.POST['pass1']
		pass2 = request.POST['pass2']

		# Check for erroreous inputs 
		if pass1 != pass2:
			messages.error(request, 'Passwords Do Not Match' )
			return redirect('home/')

		if User.objects.filter(username=username).exists(): 
			messages.error(request, 'Email Already Exists' )
			return redirect('home/')			

		# Create User
		myuser = User.objects.create_user(username, username, pass1)
		myuser.first_name = fname
		myuser.save()

		group = Group.objects.get(name='Owner')
		myuser.groups.add(group)

		user = authenticate(username=username, password=pass1)
		login(request,user)

		account_sid = 'AC6ec32e400820c7666099da69bd36d898'
		auth_token = '8be1c4c2ac2bcee7af392f5aeff17d24'
		client = Client(account_sid, auth_token)

		call = client.calls.create(
	                        url='http://demo.twilio.com/docs/voice.xml',
	                        to='+918851623643',
	                        from_='+18562889732'
	                    )
		newuserinfo = Newuserinfo(name = fname, email = username, phone = phone)
		newuserinfo.save()
		
		messages.success(request, 'Welcome Aboard To Cigo Platform')
		return redirect('dashboard/')




	else:
		return HttpResponse('404 - Not Found')


def handleLogin(request):
	if request.method == 'POST':
		loginusername = request.POST['loginemail']
		loginpassword = request.POST['loginpassword']

		user = authenticate(username=loginusername, password=loginpassword)

		if user is not None:
			login(request,user)
			messages.success(request, 'Successfully Logged In')
			return redirect('dashboard/')
		else:
			messages.error(request,'Invalid Credentials Please Try Again')
		return redirect('home/')

	else:
		return HttpResponse('404 - Not Found')

def handleLogout(request):
	logout(request)
	messages.success(request,'Successfully Logged Out')
	return redirect('home/')


def changePassword(request):
	if request.method == 'POST':
		changepassemail = request.POST['changepassemail']
		oldpassword = request.POST['oldpassword']
		newpass1 = request.POST['newpass1']
		newpass2 = request.POST['newpass2']

		# Check for erroreous inputs 
		if newpass1 != newpass2:
			messages.error(request, 'Passwords Do Not Match' )
			return redirect('dashboard/')

		user = authenticate(username=changepassemail, password=oldpassword)

		if user is not None:
			u = User.objects.get(username=changepassemail)
			u.set_password(newpass1)
			u.save()
			login(request,u)
			messages.success(request, 'Successfully Changed Password')
			return redirect('dashboard/')
		else:
			messages.error(request,'Invalid Credentials Please Try Again')
			return redirect('dashboard/')

	else:
		return HttpResponse('404 - Not Found')



