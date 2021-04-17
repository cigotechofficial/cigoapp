from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.contrib import messages 
from .models import Venue ,Employee, Menu
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from home.models import Defaultimg

from random import randint

@login_required(login_url="/home/")
@allowed_users(allowed_roles=['Owner','Admin'])
def setup(request):
	allrestaurants = Venue.objects.filter(owner=request.user)
	allemployee = Employee.objects.filter(owner=request.user)
	details = {'allrestaurants':allrestaurants, 'allemployee':allemployee}
	return render(request,'app/setup/setup.html', details)


  
 
def newvenue(request):
	if request.method == 'POST':
		venuename = request.POST['venuename']
		owner = request.user
		notables = request.POST['notables']
	
		venuedetails = Venue(venuename=venuename, owner=owner, notables=notables )
		venuedetails.save()

		messages.success(request, "Restaurant successfully saved")

	return redirect("./") 

def editvenue(request):
	if request.method == 'POST':
		venueid = request.POST['venueid']
		venuename = request.POST['editvenuename']
		owner = request.user
		notables = request.POST['editnotables']
		# cgst = request.POST['cgst']
		# sgst = request.POST['sgst']
		
		venuedetails = Venue.objects.filter(venueid=venueid)
		for venuedetail in venuedetails:
			venuedetail.venuename = venuename
			venuedetail.owner = owner
			venuedetail.notables = notables 
			venuedetail.save()


		messages.success(request, "Restaurant successfully updated")
		
	return redirect("./") 

def deletevenue(request):
	x=request.GET['id']
	venue = Venue.objects.get(venueid=x)
	venue.delete()
	messages.success(request, "Restaurant successfully deleted")


	return redirect("./") 


def addemployee(request):
	if request.method == 'POST':
		venueID = request.POST['restaurant']
		fname = request.POST['fname']
		username = request.POST['phone']
		# username = request.POST['username']
		pass1 = request.POST['pass1']
		pass2 = request.POST['pass2']

		role = request.POST['role']
		owner = request.user

		# Check for erroreous inputs 
		if pass1 != pass2:
			messages.error(request, 'Passwords Do Not Match' )
			return redirect('./')

		if User.objects.filter(username=username).exists():
			messages.error(request, 'Phone Number Already Exists' )
			return redirect('./')			

		# Create User
		myuser = User.objects.create_user(username, username, pass1)
		myuser.first_name = fname
		myuser.save()


		group = Group.objects.get(name=role)
		myuser.groups.add(group)
		venue = Venue.objects.get(venueid=venueID)

		employee = Employee(name=fname, ph=username, venue=venue, owner=owner, role=role )
		employee.save()
		messages.success(request, 'New Member Added: ' + fname + ' as ' + role + ' in ' + venue.venuename)
		return redirect('./')

	else:
		return HttpResponse('404 - Not Found')

def editemployee(request):
	if request.method == 'POST':
		employeeid = request.POST['employeeid']
		venueID = request.POST['editemployeevenue']
		fname = request.POST['editemployeename']
		username = request.POST['editemployeephone']
		# username = request.POST['username']
		pass1 = request.POST['editemployeepass1']
		pass2 = request.POST['editemployeepass2']

		role = request.POST['editemployeerole']
		owner = request.user


		# # Check for erroreous inputs 
		if pass1 != pass2:
			messages.error(request, 'Passwords Do Not Match' )
			return redirect('./')	
		
		# myuser.groups.add(group)
		venue = Venue.objects.get(venueid=venueID)

		employee=Employee.objects.get(employeeid=employeeid)
		# if employee.owner != owner :
		

		useroriginal=User.objects.filter(username=employee.ph)
		useroriginal.delete()

		employee.name=fname
		employee.ph=username
		employee.venue=venue
		employee.owner=owner
		employee.role=role
		employee.save()

		group = Group.objects.get(name=role)

		# useredit=User.objects.filter(username=username)
		# if useredit.exists():
		# 	messages.error(request, 'Phone Number Already Exists' )
		# 	return redirect('./')	

		myuser = User.objects.create_user(username, username, pass1)
		myuser.first_name = fname
		myuser.save()
		myuser.groups.add(group)

	

		# employee = Employee(name=fname, ph=username, venue=venue, owner=owner, role=role )
		# employee.save()
		# messages.success(request, 'New Member Added: ' + fname + ' as ' + role + ' in ' + venue.venuename)
		return redirect('./')

	else:
		return HttpResponse('404 - Not Found')


def deleteemployee(request):
	employeeid=request.GET['id']
	employee=Employee.objects.get(employeeid=employeeid)

	useroriginal=User.objects.filter(username=employee.ph)
	useroriginal.delete()
	messages.success(request, "Restaurant successfully deleted")

	employee.delete()

	return redirect("./") 


# def menupage(request):

# 	allrestaurants = Venue.objects.filter(owner=request.user)
# 	all_venue_names = []
# 	for rest in allrestaurants:
# 		all_venue_names.append(rest.venueid)

# 	allmenu = Menu.objects.filter(venue__in=all_venue_names).order_by('-product_id')
	
# 	myFilter = MenuFilter(request.GET, queryset=allmenu)
# 	allmenu = myFilter.qs
# 	print(myFilter)
# 	details = {'allrestaurants':allrestaurants, 'allmenu':allmenu, 'myFilter':myFilter}
# 	return render(request,'app/menu/menu.html',details)

def menupage(request):
	if request.user.groups.exists():
		group = request.user.groups.all()[0].name 

		if group == "Manager":
			manager=Employee.objects.get(ph=request.user)
			restaurant=manager.venue
			allmenu = Menu.objects.filter(venue=restaurant).filter(showtype=1)

			details = {
			'restaurant':restaurant,
			'allmenu':allmenu
			}

			

		else:
			allrestaurants = Venue.objects.filter(owner=request.user)
			allmenu = Menu.objects.filter(venue__in=allrestaurants).filter(showtype=1)

			details = {
			'allrestaurants':allrestaurants,
			'allmenu':allmenu
			}

			

		if request.method == 'POST':
			venueselect = request.POST['venueselect']
			categoryselect = request.POST['categoryselect']
			availability = request.POST['availability']

			if venueselect != "Venue": 
				allmenu=allmenu.filter(venue=venueselect)

			if categoryselect != "0":
				allmenu=allmenu.filter(category=categoryselect)		

			if availability != "Availability":
				allmenu=allmenu.filter(availability=availability)

			if group == "Manager":
				details = {
				'restaurant':restaurant,
				'allmenu':allmenu
				}
				return render(request,'app/menu/managermenu.html',details)
				
			else:
				details = {
				'allrestaurants':allrestaurants,
				'allmenu':allmenu
				# 'myFilter':myFilter
				}
				return render(request,'app/menu/menu.html',details)



			# print(venueselect,categoryselect,availability)
			return render(request,'app/menu/menu.html',details)

		if group == "Manager":
			return render(request,'app/menu/managermenu.html',details)
		else:
			return render(request,'app/menu/menu.html',details)





def additem(request):
	if request.method == 'POST':
		venueID = request.POST['restaurant']
		product_name = request.POST['name']
		category = request.POST['category'] 
		price = request.POST['price']
		description = request.POST['description']
		# img= request.POST['menuimg']
		img = request.FILES['menuimg']
		
		if img == False:
			img = Defaultimg.objects.all()[randint(0,1)].dimage


		venue = Venue.objects.get(venueid=venueID)

		item = Menu(venue=venue, product_name=product_name, category=category, price=price, description=description, image=img )
		item.save(venue)
		# print(venueID)
		messages.success(request, "Item Successfully Saved: "  )
		return redirect('../menupage')

	else:
		return HttpResponse('404 - Not Found')

def updatemenu(request):
	if request.method == 'POST':
		venueID = request.POST['restaurantupdate']
		product_name = request.POST['nameupdate']
		productid = request.POST['productid']
		category = request.POST['categoryupdate'] 
		price = request.POST['priceupdate']
		description = request.POST['descriptionupdate']
		availability = request.POST['availabilityupdate']
		
		venue = Venue.objects.get(venueid=venueID)
		item = Menu.objects.get(product_id=productid)


		if int(item.price) != int(price):
			img=item.image
			item.showtype=0
			item.save()
			newitem = Menu(venue=venue, product_name=product_name, category=category, price=price, showtype=1, description=description,image =img)
			newitem.save()
			# newitem.save(venue)

		else:
			item.venue=venue
			item.product_name=product_name
			item.category=category
			item.price=price
			item.description=description
			item.availability=availability
			item.save()

		messages.success(request, "Item Successfully Updated: "  )
		return redirect('../menupage')

	else:
		return HttpResponse('404 - Not Found')

def deletemenu(request):
	itemid=request.GET['itemid']
	item = Menu.objects.get(product_id=itemid)
	item.showtype=0
	item.save()
	messages.success(request, "Restaurant successfully deleted")

	return redirect("../")


def venueselect(request):
	
	allcat = list()

	venueid=request.GET['id']
	x=Menu.objects.filter(venue=venueid)
	categories = (x.values('category').distinct())

	for category in categories:
		allcat.append(category["category"])

	print(allcat)
	# orders=Order.objects.all()
	 
	# for ords in orders:
	# 	# print(ords.table_no)
	# 	ser = OrderSerializer(ords)
	# 	l.append(ser.data)
	# #     # print(ser.data)
	# # # print(l)
	import json
	# # print(json.dumps(t_list))
# json.dumps(l)
	return HttpResponse(json.dumps(allcat))

