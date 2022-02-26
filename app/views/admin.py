import uuid
from flask import jsonify,request,render_template,redirect,url_for
from flask_login import current_user
from app.models.usermodel import User
from app.models.orderdetailmodel import OrderDetails

hotelItem = {                   
                                "hotel aryaas":["masala dosa","ghee roast dosa","poori","idli","sambar","chammanthi","uzhunnu vada"],
                                "thaff hotel":["rice pathiri","parotta","appam","chicken curry","egg curry","chicken roast","egg chilly fry","chicken omlette","vegetable curry"],
                                "a j park":["thattu dosa","puri bhaji","hot milk"],
                                "cakes bay":["jar cake","cheese chicken burger","french fries","sharjah special shake","red velvet cake","mango cake","vancho"],
                                "cafe the pepper lounge":["bbq chicken burger","mixed fried rice","chocolate shake","veg wrap","chicken streak wrap"],
                                "brews and burgers bistro":["spaghetti chicken noodles","cheesey veg king","brews and burger heavy","french fries"],
                                "cutiepie":["vancho cake","choco chip cake"],
                                "arabian shakes":["hot and crispy bucket feast","kiwi milkshake","steamed chicken momos","papaya milkshake"],
                                "corniche":["chicken kothu parotta","nidhi parotta","kizhi parotta chicken","chicken hot and sour soup"],
                                "asado cafe":["arabic style barbecue","cheesy lucy","mac and cheese","fried ice cream","coconut sundae"],
                                "bayroute bistro":["chicken cream soup","caesar salad","peanut chicken","veg mappas"],
                                "kream korner":["sweet corn veg soup","beef chilli fry","ginger prawns","dragon chicken","ghee rice"],
                                "domino's pizza":["pepper barbecue chicken","indo fusion chicken pizza","margherita","deluxe veggie"],
                                "ramada":["kung pao Chicken","gaithod","carne asada","masala peanuts","maharaja platter"],
                                "dessi cuppa":["royal falooda","motojojo","chicken crumbs","veg crumbs"],
                                "cafe pumpkin":["tex mex nachos chicken","dark chocolate marquse","milk chocolate marquse","russian honey pastry"],
                                "achayans":["pomegranate juice","achayan's meri boy falooda","special fruit salad","chicken sandwich with Wine and French Fries"],
                                "kfc":["chick'n dip combo","stay home bucket","family feast"]}


items=[]

def admincheck():
	return render_template("admin.html")

def view_order_details():
	#function to view the user orders(admin privilege)
	orderitems = OrderDetails.objects.all()
	return render_template("orderplaced.html",orderitems=orderitems)


def addhotel():
	#function to add a hotel(admin privilege)
	if request.method == 'POST':
		global hotelname
		hotelname=request.form["hotelname"]
		return render_template("addhotel.html")
	else:
		return render_template("addhotel.html")


def additems():
	#function to add items for the newly added restaurant
	if request.method == 'POST':
		global itemname
		itemname = request.form["itemname"]
		print(itemname)
		items.append(itemname)
		print(items)
		return render_template("addhotel.html")

def finishedit():
	#to mark the end of restaurant adding process
	if request.method== "POST":
		hotelItem[hotelname]=items 
		return render_template("addhotel.html")

def removehotel():
	#function to remove a hotel(admin privilege)
	if request.method == 'POST':
		hotelname=request.form["hotelname"]
		del hotelItem[hotelname]
		return render_template("removehotel.html")
	else:
		return render_template("removehotel.html")