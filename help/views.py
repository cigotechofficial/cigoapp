from django.shortcuts import render,HttpResponse,redirect
from .models import Tutorial
from twilio.rest import Client
from django.contrib import messages
from .models import Calldetail

def tutorials(request):
	tutorials = Tutorial.objects.all()
	print(tutorials[0].videoname)
	
	return render(request,'app/help/tutorials/tutorials.html', {'tutorials':tutorials})

def productspecialist(request):
	return render(request,'app/help/call/call.html')

def call(request):

	if request.method == 'POST':
		name = request.POST['name']
		phone = request.POST['phone']
		calldetails = Calldetail(name=name, phone=phone)
		calldetails.save()

		account_sid = 'AC336251d106634cc4399f478e0c50b771'
		auth_token = '3b5559481af33e5b6424b2eeb068b79e'
		client = Client(account_sid, auth_token)

		call = client.calls.create(
	                        url='http://demo.twilio.com/docs/voice.xml',
	                        to='+918851623643',
	                        from_='+13367016396'
	                    )
		# print(name, phone)
		print(call.sid)
		messages.info(request, 'We will get back to you in few mins!')
	return redirect('/help/productspecialist')