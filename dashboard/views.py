from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from app_eordering.models import Order,Waiter,ArchiveOrder,Feedback,CustomerAuthentication,VerifyOrder
from app_eordering.serializer import OrderSerializer,TableSerializer,WaiterSerializer,VerifyOrderSerializer
from setup.models import Menu, Venue, Employee
from home.models import Gst
import json
from django.contrib.auth.models import User
from setup.models import Venue
from datetime import datetime, timedelta
import pytz
from django.contrib import messages


import random
import string 




@login_required(login_url="/home/")
# @allowed_users(allowed_roles=['Owner','Admin', 'Waiter', 'Manager'])
def dashboard(request):
	if request.user.groups.exists():
		group = request.user.groups.all()[0].name 

		if group == 'Manager':

			manager = Employee.objects.get(ph=request.user.username)
			manager_venueid=manager.venue.venueid
			venue=Venue.objects.get(venueid=manager_venueid)
			tablenos=list(range(1, venue.notables+1))


			table_selected=0
			table_qr='none'

			if request.method == 'POST':
				table_selected=request.POST['tablenoselect']
				restaurantid = venue.venueid

				key = ''
				for i in range(15):
					key += random.choice(string.ascii_lowercase + string.digits)

				hashingcode = key
				
				filtereddata=CustomerAuthentication.objects.filter(restaurant=venue).filter(table_no=table_selected)

				if len(filtereddata) == 0: 
					customerauthentication = CustomerAuthentication(restaurant=venue, table_no=table_selected, hashcode=hashingcode)
					customerauthentication.save()

				else:
					hashingcode=filtereddata[0].hashcode
				

				table_qr = 'cigo.co.in/customerapp/' + str(restaurantid) + '/' + str(table_selected) + '/' + hashingcode +'/welcome'
				# table_qr = 'https://cigo.co.in/' + str(restaurantid) + '/' + str(table_selected) + '/' + hashingcode

			tableparams={
			'restaurantname':venue.venuename,
			'tablenos':tablenos,
			'table_selected':table_selected,
			'table_qr':table_qr
			}

			return render(request,'app/dashboard/managerDashboard.html',tableparams)

		if group == 'Chef':
			return render(request,'app/dashboard/chefDashboard.html')		

		if group == 'Waiter':

			waiter = Employee.objects.get(ph=request.user.username)
			waiter_venueid=waiter.venue.venueid
			venue=Venue.objects.get(venueid=waiter_venueid)
			tablenos=list(range(1, venue.notables+1))


			table_selected=0
			table_qr='none'
			if request.method == 'POST':
				table_selected=request.POST['tablenoselect']
				restaurantid = venue.venueid

				key = ''
				for i in range(15):
					key += random.choice(string.ascii_lowercase + string.digits)

				hashingcode = key
				
				filtereddata=CustomerAuthentication.objects.filter(restaurant=venue).filter(table_no=table_selected)

				if len(filtereddata) == 0: 
					customerauthentication = CustomerAuthentication(restaurant=venue, table_no=table_selected, hashcode=hashingcode)
					customerauthentication.save()

				else:
					hashingcode=filtereddata[0].hashcode
				

				table_qr = 'cigo.co.in/customerapp/' + str(restaurantid) + '/' + str(table_selected) + '/' + hashingcode +'/welcome'
				# table_qr = 'https://cigo.co.in/' + str(restaurantid) + '/' + str(table_selected) + '/' + hashingcode
			# ---------------------------------------------end session waiter ---------------------------------------------------
			orders = Order.objects.filter(restaurant=waiter_venueid)
			venue = Venue.objects.get(venueid=waiter_venueid)

			t_list = list()
			tables = orders.values('table_no').distinct()

			tax = Gst.objects.all()[0]
			cgst = tax.cgst
			sgst = tax.sgst
			
			for table in tables:

				l = list()
				table_orders=orders.filter(table_no=table['table_no'])
				
				for ords in table_orders:
					totals = dict()
					
					total_cgst = 0 
					total_sgst = 0
					for k,v in list(json.loads(ords.items_json).items()):
						item_id = k[2:]
						qty, item = v
						# print(item_id)
						prod_price = Menu.objects.filter(product_id=item_id)[0].price  

						prod_total = qty*prod_price
						
						totals.update({k:[prod_price, prod_total]})
					ser = TableSerializer(ords)
					ser_dict = dict(ser.data)
					ser_dict["prices"] = totals
					ser_dict["venue"] = waiter_venueid
					
					l.append(ser_dict)
				l.append(table)
				t_list.append(l)

			dumplist = json.dumps(t_list)
			# print(t_list)

			tableparams={
			'restaurantname':venue.venuename,
			'cgst':cgst,
			'sgst':sgst,
			'tablenos':tablenos,
			'table_selected':table_selected,
			'table_qr':table_qr,
			't_list':t_list,
			'dumplist':dumplist

			}
			return render(request,'app/dashboard/waiterDashboard.html',tableparams)

		daily_prices = []
		dates = []
		happinesslist = []
		feedbacklist = []
		graphdata = []
		hapinessindex = 0
		feedbackno = 0

		if group == 'Owner':
			uservenues = Venue.objects.filter(owner=request.user)

			if len(uservenues) == 0:
				return HttpResponseRedirect('../setup')

			restaurantid = uservenues[0].venueid 
			todate = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
			fromdate = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')

			if request.method == 'POST':
				restaurantid=request.POST['restaurant']
				fromdate=request.POST['fromdate']
				todate=request.POST['todate']

			fromdate=datetime.strptime(fromdate,'%Y-%m-%d').replace(tzinfo=pytz.UTC).date()
			todate=datetime.strptime(todate,'%Y-%m-%d').replace(tzinfo=pytz.UTC).date()

			venue = Venue.objects.get(venueid=restaurantid)
		# ---------------------------------------------Revenue Chart Start-----------------------------------------------------------------
			orders = ArchiveOrder.objects.filter(restaurant=venue)

			allorderlen= len(orders)
			# print(allorderlen)
			# for order in orders:
			# 	ordertime=order.timestamp

			cur_date = fromdate
			# daily_prices = []
			while cur_date < todate:
				day_total = 0

				for order in orders:
					orderdate=order.timestamp.date()
					if orderdate == cur_date:
						orders_dict = json.loads(order.items_json)
						for k in orders_dict.keys():

							item_id = k[2:]

							qty, item = orders_dict[k]
							prod_price = Menu.objects.filter(product_id=item_id)[0].price
							prod_total = qty*prod_price

							day_total = day_total + prod_total

				daily_prices.append(day_total)    
				dates.append(cur_date.strftime('%d/%m/%Y'))      
				cur_date += timedelta(days=1)

				avg_dailyrevenue = round(sum(daily_prices) / len(daily_prices) )

		# -----------------------------------------------Revenue Chart End ----------------------------------------------------------------
		# --------------------------------------------------Feedback Start -----------------------------------------------------------------	
			feedbacks = Feedback.objects.filter(restaurant=venue)
			# feedbacktime=feedback.timestamp.date()
			


			for feedback in feedbacks:
				feedbackdate=feedback.timestamp.date()
				

				if fromdate <= feedbackdate and feedbackdate <= todate:
					happinesslist.append(feedback.happiness)
					feedbacklist.append(feedback.feedbacktext)




			awesomecount=((happinesslist).count('Awesome'))
			satisfiedcount=((happinesslist).count('Satisfied'))
			unsatisfiedcount=((happinesslist).count('Unsatisfied'))

			hapinessindex = round((awesomecount+(satisfiedcount*0.5))/((awesomecount+satisfiedcount+unsatisfiedcount)+0.000001)*100)

			graphdata.append(awesomecount)
			graphdata.append(satisfiedcount)
			graphdata.append(unsatisfiedcount)

			while("" in feedbacklist):
				feedbacklist.remove("") 
			
			feedbackno = len(feedbacklist)
	# ------------------------------------------------Feedback End---------------------------------------------------------------
			allrestaurants = Venue.objects.filter(owner=request.user) 
			params={
			'restaurantname':venue.venuename,
			'avg_dailyrevenue':avg_dailyrevenue,
			'allorderlen':allorderlen,
			'allrestaurants':allrestaurants,
			'daily_prices':daily_prices,
			'dates':dates,
			'graphdata':graphdata,
			'feedbacklist':feedbacklist,
			'hapinessindex':hapinessindex,
			'feedbackno':feedbackno
			}
			return render(request,'app/dashboard/ownerDashboard.html', params)

		else:
			return HttpResponse('You are not allowed to see dashboard')







@login_required(login_url="/home/")
@allowed_users(allowed_roles=['Owner','Admin','Manager'])
def orderhistory(request):
	items = []
	qtys = []
	prod_totals = []
	orderids = []
	ordertimestaps = []
	
	if request.method == 'POST':
		restaurantid=request.POST['restaurant']
		fromdate=request.POST['fromdate']
		todate=request.POST['todate']

		fromdate=datetime.strptime(fromdate,'%Y-%m-%d').replace(tzinfo=pytz.UTC).date()
		todate=datetime.strptime(todate,'%Y-%m-%d').replace(tzinfo=pytz.UTC).date()

		venue = Venue.objects.get(venueid=restaurantid)
		orders = ArchiveOrder.objects.filter(restaurant=venue)

		for order in orders:
			orderdate=order.timestamp.date()

			if fromdate <= orderdate and orderdate <= todate:
				
				orders_dict = json.loads(order.items_json)
				for k in orders_dict.keys():
					item_id = k[2:]
					qty, item = orders_dict[k]
					prod_price = Menu.objects.filter(product_id=item_id)[0].price
					prod_total = qty*prod_price

					items.append(item)
					qtys.append(qty)
					prod_totals.append(prod_total)
					orderids.append(order.order_id)
					ordertimestaps.append(orderdate)

	mylist = zip(items, qtys, prod_totals, ordertimestaps, orderids)
	allrestaurants = Venue.objects.filter(owner=request.user)

	
	params ={
	'allrestaurants':allrestaurants,
	'mylist':mylist
	}
	return render(request,'app/dashboard/orderhistory.html',params)



def sessionDetailsManager(request):
	t_list = list()
	manager = Employee.objects.get(ph=request.user.username)
	tables = Order.objects.filter(restaurant=manager.venue).values('table_no').distinct()

	for table in tables:

		l = list()
		table_orders=Order.objects.filter(restaurant=manager.venue).filter(table_no=table['table_no'])
		# print(table_orders)
		for ords in table_orders:
			# print("ORDER")
			totals = dict()
			for k,v in list(json.loads(ords.items_json).items()):
				item_id = k[2:]
				qty, item = v
			# qty, item = list(json.loads(ords.items_json).values())[0]
				prod_price = Menu.objects.filter(product_id=item_id)[0].price
				prod_total = qty*prod_price
			# table_no = ords.table_no
				# print(item, qty, prod_price, prod_total)
				totals.update({k:[prod_price, prod_total]})
			# entry = {"table_no":table_no,
			#         "item":item,
			#         "qty":qty,
			#         "prod_price":prod_price,
			#         "prod_total":total}
			# print(entry)
			ser = TableSerializer(ords)
			ser_dict = dict(ser.data)
			# print(json.dumps([ser.data]+totals))
			ser_dict["prices"] = totals
			# print(ser_dict)
			l.append(ser_dict)
			# print(ser)
		l.append(table)
		# print(l)
		t_list.append(l)
	# for ords in orders:
	#     # print(ords.table_no)
	#     ser = OrderSerializer(ords)
	#     l.append(ser.data)
	#     # print(ser.data)
	# # print(l)
	
   # print(json.dumps(t_list))
	# print(t_list)
	return HttpResponse(json.dumps(t_list))

def getNewOrderManager(request):
	l = list()
	manager = Employee.objects.get(ph=request.user.username)
	orders=Order.objects.filter(restaurant=manager.venue)
	 
	for ords in orders:
		# print(ords.table_no)
		ser = OrderSerializer(ords)
		l.append(ser.data)
	#     # print(ser.data)
	# # print(l)
	import json
	# print(json.dumps(t_list))

	return HttpResponse(json.dumps(l))

def deleteOrder(request):
	# print(request.GET['id'])
	employee = Employee.objects.get(ph=request.user.username)
	# print(employee)
	orders = Order.objects.filter(table_no = request.GET['id']).filter(restaurant=employee.venue)
	
	
	# print()
	allitems=list()
	tabletotal = 0
	for order in orders:
		allitems.append(order.items_json)

		ordertotal=0
		orders_dict = json.loads(order.items_json)
		for k in orders_dict.keys():
			item_id = k[2:]
			qty, item = orders_dict[k]
			prod_price = Menu.objects.filter(product_id=item_id)[0].price
			prod_total = qty*prod_price
			ordertotal = ordertotal + prod_total

		tabletotal = tabletotal + ordertotal
		order.delete()

	tax = Gst.objects.all()[0]
	cgst = tax.cgst
	sgst = tax.sgst
	totalamount = tabletotal + (tabletotal*cgst/100) + (tabletotal*sgst/100)
	
	verifyorder=VerifyOrder(items_json=allitems, totalamount=totalamount, restaurant=employee.venue)
	verifyorder.save()

	custauth = CustomerAuthentication.objects.filter(table_no = request.GET['id']).filter(restaurant=employee.venue)
	custauth.delete()
	return HttpResponse('true')

def getWaiterCall(request):
	l = list()
	waiter=Waiter.objects.all()
	
	for call in waiter:
		# print(ords.table_no)
		ser = WaiterSerializer(call)
		l.append(ser.data)
	#     # print(ser.data)
	# print(l)
	import json
	# print(json.dumps(t_list))

	return HttpResponse(json.dumps(l))

def deletewaiter(request):
	try:
		# print(request.GET['id'])
		waiter = Waiter.objects.filter(id = request.GET['id'])
		# print(waiter)
		for x in waiter:
			x.delete()
		return HttpResponse('true')
	except:
		return HttpResponse('false') 


def neworderwaiter(request):
	l = list()
	waiter = Employee.objects.get(ph=request.user.username)
	venue=Venue.objects.get(venueid=waiter.venue.venueid)
	orders=Order.objects.filter(restaurant=venue)

	for ords in orders:

		ser = OrderSerializer(ords)
		l.append(ser.data)
	
	

	return HttpResponse(json.dumps(l))

# --------------------------------------------------------For Waiter Start-----------------------------------------------------------------

def shiftcooking(request):
	if request.method == 'POST':
		orderid = request.POST['neworderid']
		order=Order.objects.get(order_id=orderid)
		order.status=1
		order.save()

	return HttpResponseRedirect('../#neworder')

def served(request):
	if request.method == 'POST':
		orderid = request.POST['cookingorderid']
		# print(orderid)
		order=Order.objects.get(order_id=orderid)
		order.status=2
		order.save()

	return HttpResponseRedirect('../#neworder')

# ----------------------------------------------------------For Waiter End -------------------------------------------------------------
def shifttocookingmanager(request):

	order = Order.objects.filter(order_id = request.GET['id'])
	# print(order[0].status)
	for x in order:
		x.status=1
		x.save()
		# print(x.status)

	return HttpResponse('true')

def shifttoservedmanager(request):

	order = Order.objects.filter(order_id = request.GET['id'])
	# print(order[0].status)
	for x in order:
		x.status=2
		x.save()
		# print(x.status)

	return HttpResponse('true')


# -------------------------------------------------------------Verify Payment Table Start-----------------------------------------------------------
def verifypaymenttable(request):
	l = list()
	employee = Employee.objects.get(ph=request.user.username) 
	verifyorders=VerifyOrder.objects.filter(restaurant=employee.venue)
	 
	for ords in verifyorders:

		ser = VerifyOrderSerializer(ords)
		l.append(ser.data)

	return HttpResponse(json.dumps(l))


# -------------------------------------------------------------Verify Payment Table End-----------------------------------------------------------

def shifttoverified(request):

	order = VerifyOrder.objects.filter(order_id = request.GET['id'])
	# print(order[0].status)
	for x in order:
		x.status=1
		x.save()
		# print(x.status)

	return HttpResponse('true')