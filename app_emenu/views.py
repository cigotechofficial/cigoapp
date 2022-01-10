from setup.models import Menu
from django.shortcuts import render
from setup.models import Venue

def welcome(request,restaurantidslug):
	venue = Venue.objects.get(venueid=restaurantidslug)
	dicts={
	'restaurantname':venue.venuename,
	'restaurantidslug':restaurantidslug,

	}
	return render(request,'app_emenu/welcome.html',dicts) 



def emenu(request,restaurantidslug):

	venue = Venue.objects.get(venueid=restaurantidslug)
	restaurantname = venue.venuename
	emenutheme = venue.emenu_theme

	allProds = []

	catprods = Menu.objects.filter(venue=restaurantidslug).filter(showtype=1).filter(availability="ava").values('category')
	cats = {item['category'] for item in catprods}

	for cat in cats:
		prod = Menu.objects.filter(venue=restaurantidslug).filter(showtype=1).filter(availability="ava").filter(category=cat )
		allProds.append(prod)

	params={
	'restaurantname':restaurantname,
	'allProds': allProds,
	'restaurantidslug':restaurantidslug,
	}
	if emenutheme == 1:
		return render(request,'app_emenu/menu.html', params)

	elif emenutheme == 2:
		return render(request,'app_emenu2/menu.html', params)

	elif emenutheme == 3:
		return render(request,'app_emenu3/menu.html', params)



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