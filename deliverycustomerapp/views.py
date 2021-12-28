from django.contrib.auth.models import User
from setup.models import Menu
from home.models import Gst
from django.contrib.auth import logout
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import Group
from setup.models import Venue
from .models import DeliveryOrder,ArchiveDeliveryOrder
from deliverydashboard.models import Discount
import json
from home.models import Gst
from twilio.rest import Client

def deliverycustomerapp(request,restaurantidslug):
	
	restaurantname = Venue.objects.get(venueid=restaurantidslug).venuename

	allProds = []

	catprods = Menu.objects.filter(venue=restaurantidslug).filter(showtype=1).filter(availability="ava").values('category')
	cats = {item['category'] for item in catprods}

	for cat in cats:
		prod = Menu.objects.filter(venue=restaurantidslug).filter(showtype=1).filter(availability="ava").filter(category=cat )
		# prod = Menu.objects.filter(category=cat, availability='ava')
		allProds.append(prod)

	# print(allProds[1])
	params={
	'restaurantname':restaurantname,
	'allProds': allProds,
	'restaurantidslug':restaurantidslug,
	}
 
	return render(request,'deliverycustomerapp/deliverycustomerapp.html', params)

def checkout(request,restaurantidslug,):
	tax = Gst.objects.all()[0]
	cgstval = tax.cgst
	sgstval = tax.sgst
	paymentphoneno = Venue.objects.get(venueid=restaurantidslug).paymentphoneno
	try:
		discountmodel = Discount.objects.get(restaurant=restaurantidslug)
		discount = discountmodel.discount
	except:
		discount = 30
	params={
	'restaurantid':restaurantidslug,
	'discount':discount,
	'cgstval':cgstval,
	'sgstval':sgstval,
	'paymentphoneno':paymentphoneno,
	}
	if request.method=="POST":
		items_json = request.POST.get('itemsJson', '')
		status = 0
		
		order = DeliveryOrder(items_json=items_json, restaurant=venue, status=status)

		order.save()
		thank = True
		orderdone = True
		# id = order.order_id
		return render(request, 'deliverycustomerapp/checkout.html', {'thank':thank, 'restaurantid':restaurantidslug})
	return render(request,'deliverycustomerapp/checkout.html', params)


def address(request,restaurantidslug):
	tax = Gst.objects.all()[0]
	cgstval = tax.cgst
	sgstval = tax.sgst
	try:
		discountmodel = Discount.objects.get(restaurant=restaurantidslug)
		discount = discountmodel.discount
	except:
		discount = 30
	params={
	'restaurantid':restaurantidslug,
	'discount':discount,
	'cgstval':cgstval,
	'sgstval':sgstval,
	}
	if request.method=="POST":
		items_json = request.POST.get('itemsJson', '')
		print(items_json)
		venue = Venue.objects.get(venueid=restaurantidslug)
		name = request.POST.get('name', '')
		phone = request.POST.get('phone', '')
		address = request.POST.get('address', '')
		order = DeliveryOrder(items_json=items_json, restaurant=venue, name=name, phone=phone, address=address)
		order.save()

		archiveorder = ArchiveDeliveryOrder(items_json=items_json, restaurant=venue, name=name, phone=phone, address=address)
		archiveorder.save()
		thank = True
		orderdone = True
		# id = order.order_id
		account_sid = 'ACd9091a3d9a2318e52141f22b2f55221c'
		auth_token = 'de41b86cc18874cc03643a15edf9c1af'
		client = Client(account_sid, auth_token)

		call = client.calls.create(
	                        url='http://demo.twilio.com/docs/voice.xml',
	                        to='+918851623643',
	                        from_='+13347218681'
	                    )
		
		return render(request, 'deliverycustomerapp/address.html', {'thank':thank, 'restaurantid':restaurantidslug})
	return render(request,'deliverycustomerapp/address.html', params)

def thankyou(request,restaurantidslug):

	return render(request,'deliverycustomerapp/thankyou.html')


