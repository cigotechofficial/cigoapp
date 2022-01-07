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



def emenu(request,restaurantidslug):

	venue = Venue.objects.get(venueid=restaurantidslug)
	restaurantname = venue.venuename
	emenutheme = venue.emenu_theme

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
	if emenutheme == 1:
		return render(request,'onlymenuapp/menu.html', params)

	else:
		return render(request,'onlymenuapp2/menu.html', params)




# def customerapp(request,restaurantidslug):

# 	restaurantname = Venue.objects.get(venueid=restaurantidslug).venuename

# 	allProds = [] 

# 	catprods = Menu.objects.filter(venue=restaurantidslug).filter(showtype=1).filter(availability="ava").values('category')
# 	cats = {item['category'] for item in catprods}

# 	catorder_str = Venue.objects.filter(venueid=restaurantidslug)[0].category_list_sorted
# 	catorder_list = [c.strip() for c in catorder_str.split(',')]

# 	for cat in catorder_list:
# 		prod = Menu.objects.filter(venue=restaurantidslug).filter(showtype=1).filter(availability="ava").filter(category=cat ).order_by('serialno')
# 		# prod = Menu.objects.filter(venue=restaurantidslug).filter(showtype=1).filter(availability="ava").filter(category=cat )
# 		# prod = Menu.objects.filter(category=cat, availability='ava')
# 		allProds.append(prod)

# 	allcustomisablefields = {}

# 	allcustomisableitems = Menu.objects.filter(venue=restaurantidslug).filter(showtype=1).filter(availability="ava").filter(customisable=1)
	
# 	for customisableitem in allcustomisableitems:
# 		customisablefield = CustomItem.objects.filter(product_id=customisableitem.product_id)
# 		allcustomisablefields[customisableitem.product_id] = customisablefield

# 	# print(allcustomisablefields)
# 	params={
# 	'allcustomisablefields':allcustomisablefields,
# 	'restaurantname':restaurantname,
# 	'allProds': allProds,
# 	'restaurantidslug':restaurantidslug,
# 	}
 
# 	return render(request,'onlymenuapp2/menu.html', params)