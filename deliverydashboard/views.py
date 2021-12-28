from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from django.contrib import messages 
from setup.models import Menu,Venue,Employee
from django.contrib.auth import authenticate, login, logout
from deliverycustomerapp.models import DeliveryOrder
import json
from deliverycustomerapp.serializer import DeliveryOrderSerializer
from .models import Discount

@login_required(login_url="/home/")
# @allowed_users(allowed_roles=['Owner','Admin'])
def deliverydashboard(request):

	if request.user.groups.exists():
		group = request.user.groups.all()[0].name 

		if group == 'Manager':

			manager = Employee.objects.get(ph=request.user.username)
			manager_venueid=manager.venue.venueid
			venue=Venue.objects.get(venueid=manager_venueid)

			try:
				discountmodel = Discount.objects.get(restaurant=venue)
				discount = discountmodel.discount
				# print(discount) 
			except:
				discount = 30
				# print("except")
			params = {
			'restaurantname':venue.venuename,
			'discount':discount,
			'venueid':venue.venueid
			}
			return render(request,'app/deliverydashboard/managerdeliverydashboard.html',params)



		if group == 'Owner':

			venue= Venue.objects.filter(owner=request.user)
			try:
				discountmodel = Discount.objects.get(restaurant=venue[0])
				discount = discountmodel.discount
				# print(discount) 
			except:
				discount = 30
				# print("except")
			params = {
			'restaurantname':venue[0].venuename,
			'discount':discount,
			'venueid':venue[0].venueid
			}
			return render(request,'app/deliverydashboard/deliverydashboard.html',params)


def getNewDeliveryOrder(request):

	l = list()

	venue=Venue.objects.filter(owner=request.user)
	
	try:
		orders=DeliveryOrder.objects.filter(restaurant=venue[0])
	except:
		manager = Employee.objects.get(ph=request.user.username)
		manager_venueid=manager.venue.venueid
		venue=Venue.objects.get(venueid=manager_venueid)
		orders=DeliveryOrder.objects.filter(restaurant=venue)
	

	for ords in orders:
		# print(ords)
		ser = DeliveryOrderSerializer(ords)
		l.append(ser.data)
	    # print(ser.data)
	# print(l)
	import json
	# print(json.dumps(t_list))

	return HttpResponse(json.dumps(l))

def shifttodelivery(request):
	order = DeliveryOrder.objects.filter(order_id = request.GET['id'])
	# print(order[0].status)
	for x in order:
		x.status=1
		x.save()
		# print(x.status)

	return HttpResponse('true')

def deletedelivery(request):
	order = DeliveryOrder.objects.filter(order_id = request.GET['id'])
	# print(order[0].status)
	for x in order:
		# x.status=1
		x.delete()
		# print(x.status)

	return HttpResponse('true')

def deliverydiscount(request):
	if request.method=="POST":
		discountrate = request.POST.get('discount', '')
		venue= Venue.objects.filter(owner=request.user)
		# print(venue,discountrate)
	
		try:
			# print("1")
			d = Discount.objects.get(restaurant=venue[0])
			# print(d)
			d.discount=discountrate
			d.save()

		except Discount.DoesNotExist:
			# print("2")
			d = Discount(restaurant=venue[0], discount=discountrate)
			d.save()

		return HttpResponseRedirect('../')

