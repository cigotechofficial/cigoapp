from setup.models import Menu
from home.models import Gst
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Order,ArchiveOrder,Waiter,Feedback,CustomerAuthentication
from setup.models import Venue
import json

def welcome(request,restaurantidslug,tableno,hashcode):
	custauth= CustomerAuthentication.objects.filter(hashcode=hashcode).filter(table_no=tableno).filter(restaurant=restaurantidslug)
	venue = Venue.objects.get(venueid=restaurantidslug)
	if len(custauth) != 0:
		dicts={
		'restaurantname':venue.venuename,
		'restaurantidslug':restaurantidslug,
		'tableno':tableno,
		'hashcode':hashcode

		}
		return render(request,'app_eordering/welcome.html',dicts)
	else:
		return HttpResponse("Invalid") 

def logingmail(request, restaurantidslug):
	params={
	'restaurantid':restaurantidslug
	}
	return render(request,'app_eordering/logingmail.html',params) 
	
def customerapp(request,restaurantidslug,tableno,hashcode):

	custauth= CustomerAuthentication.objects.filter(hashcode=hashcode).filter(table_no=tableno).filter(restaurant=restaurantidslug)

	restaurantname = Venue.objects.get(venueid=restaurantidslug).venuename

	if len(custauth) != 0:	
		previousorder = Order.objects.filter(restaurant=restaurantidslug).filter(table_no=tableno)
		if not previousorder:
			orderdone = False
		else:
			orderdone = True

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
		'orderdone':orderdone,
		'restaurantidslug':restaurantidslug,
		'tableno':tableno,
		'hashcode':hashcode
		}
	 
		return render(request,'app_eordering/menu.html', params)

	else:
		return HttpResponse("Invalid")

def redirect(request,restaurantidslug,tableno,hashcode):
	return render(request,"app_eordering/redirect.html")
	
def checkout(request,restaurantidslug,tableno,hashcode):
	custauth= CustomerAuthentication.objects.filter(hashcode=hashcode).filter(table_no=tableno).filter(restaurant=restaurantidslug)

	if len(custauth) != 0:
		params={
		'restaurantid':restaurantidslug, 
		'tableno':tableno,
		'hashcode':hashcode,
		}
		if request.method=="POST":
			items_json = request.POST.get('itemsJson', '')
			# table_no = extract_table_no(table_no_prime)
			# status = request.POST.get('status', '')
			table_no = tableno
			status = 0
			venue = Venue.objects.get(venueid=restaurantidslug)
			order = Order(items_json=items_json, restaurant=venue, table_no=table_no, status=status)
			archiveorder = ArchiveOrder(items_json=items_json, restaurant=venue, table_no=table_no, status=status)

			print(items_json)
			order.save()
			archiveorder.save()
			thank = True
			orderdone = True
			# id = order.order_id
			return render(request, 'app_eordering/orderpage.html', {'thank':thank, 'restaurantid':restaurantidslug, 'tableno':tableno, 'hashcode':hashcode})
		return render(request,'app_eordering/orderpage.html', params)
	else:
		return HttpResponse("Invalid")


def callwaiter(request,restaurantidslug,tableno,hashcode):
    # table_no_prime = (request.GET['tableNo'])
    # table_no = extract_table_no(table_no_prime)
    # print(table_no)
    table_no_prime = tableno
    wcall = 0

        
    waiter = Waiter(table_no_w=table_no_prime, wcall=wcall)
    waiter.save()
    return HttpResponse('True') 


def status(request,restaurantidslug,tableno,hashcode):
	custauth= CustomerAuthentication.objects.filter(hashcode=hashcode).filter(table_no=tableno).filter(restaurant=restaurantidslug)

	if len(custauth) != 0:
		orders = Order.objects.filter(restaurant=restaurantidslug).filter(table_no=tableno)
		orderstatus=[]
		qtylist=[]
		itemlist=[]
		# pricedict=[]
		for order in orders:
			orderstatus.append(order.status)
			orders_dict = json.loads(order.items_json)
			for k in orders_dict.keys():
				qty, item = orders_dict[k]
				qtylist.append(qty)
				itemlist.append(item)

		if min(orderstatus)==0:
			stepone = "active"
			steptwo = ""
			stepthree = ""		

		if min(orderstatus)==1:
			stepone = "active"
			steptwo = "active"
			stepthree = ""		

		if min(orderstatus)==2:
			stepone = "active"
			steptwo = "active"
			stepthree = "active"

		zipped=zip(itemlist,qtylist)		
		params ={
		'stepone':stepone,
		'steptwo':steptwo,
		'stepthree':stepthree,
		'zipped':zipped,
		}
		return render(request,'app_eordering/status.html',params)
	else:
		return HttpResponse("Invalid")

def feedback(request,restaurantidslug,tableno,hashcode):
	custauth= CustomerAuthentication.objects.filter(hashcode=hashcode).filter(table_no=tableno).filter(restaurant=restaurantidslug)

	if len(custauth) != 0:
		if request.method == 'POST':
				happinessf = request.POST['happiness']
				feedbackf = request.POST['feedback']

				venue = Venue.objects.get(venueid=restaurantidslug)

				form = Feedback(restaurant=venue,happiness=happinessf,feedbacktext=feedbackf)
				form.save()

				return HttpResponseRedirect('../payment')

		return render(request,'app_eordering/feedback.html')
	else:
		return HttpResponse("Invalid")


def payment(request,restaurantidslug,tableno,hashcode):
	custauth= CustomerAuthentication.objects.filter(hashcode=hashcode).filter(table_no=tableno).filter(restaurant=restaurantidslug)

	if len(custauth) != 0:
		orders = Order.objects.filter(restaurant=restaurantidslug).filter(table_no=tableno)
		itemlist=[]
		qtylist=[]
		pricelist=[]
		prodtotallist=[]
		subtotal = 0
		for order in orders:
			orders_dict = json.loads(order.items_json)
			for k in orders_dict.keys():
				item_id = k[2:]
				qty, item = orders_dict[k]
				prod_price = Menu.objects.filter(product_id=item_id)[0].price   
				prod_total = qty*prod_price
				subtotal = subtotal + prod_total

				itemlist.append(item)
				qtylist.append(qty) 
				pricelist.append(prod_price)
				prodtotallist.append(prod_total)

		zipped=zip(itemlist,pricelist,qtylist,prodtotallist)

		tax = Gst.objects.all()[0]
		cgstval = tax.cgst
		sgstval = tax.sgst

		cgst=round(subtotal*cgstval/100)
		sgst=round(subtotal*sgstval/100)

		total = round(subtotal+cgst+sgst)
		params ={
		'zipped':zipped,
		'subtotal':subtotal,
		'cgstval':cgstval,
		'sgstval':sgstval,	
		'cgst':cgst,
		'sgst':sgst,
		'total':total
		}
		return render(request,'app_eordering/payment.html',params)
	else:
		return HttpResponse("Invalid")

