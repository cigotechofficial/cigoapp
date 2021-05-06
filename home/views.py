from django.shortcuts import render,HttpResponse,redirect
from .models import Contactus
from django.contrib import messages 
from twilio.rest import Client

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
		account_sid = 'AC336251d106634cc4399f478e0c50b771'
		auth_token = '3b5559481af33e5b6424b2eeb068b79e'
		client = Client(account_sid, auth_token)

		call = client.calls.create(
	                        url='http://demo.twilio.com/docs/voice.xml',
	                        to='+918851623643',
	                        from_='+13367016396'
	                        )

		messages.success(request, "We Will Contact You")

	return redirect("./") 