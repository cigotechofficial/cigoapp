from django.contrib.auth.models import User
from setup.models import Menu
from home.models import Gst
from django.contrib.auth import logout
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import Group
from setup.models import Venue
import json

def welcome(request,restaurantidslug):
	venue = Venue.objects.get(venueid=restaurantidslug)
	dicts={
	'restaurantname':venue.venuename,
	'restaurantidslug':restaurantidslug,

	}
	return render(request,'onlymenuapp/welcome.html',dicts) 



def customerapp(request,restaurantidslug):

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
 
	return render(request,'onlymenuapp/menu.html', params)



