from django.shortcuts import render,HttpResponse,redirect
from .models import Contactus
from django.contrib import messages 

def home(request):
	return render(request,'home/home.html')


def contactus(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		ph = request.POST['ph']
		message = request.POST['message']
	
		contactus = Contactus(name=name, email=email, phone=ph, message=message )
		contactus.save()

		messages.success(request, "We Will Contact You")

	return redirect("./") 