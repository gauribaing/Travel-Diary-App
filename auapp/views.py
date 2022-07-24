from django.shortcuts import render, redirect
import requests
import folium
import geocoder
from .forms import TripForm
from .models import TripModel
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.mail import send_mail
from random import randrange

def home(request):
	if request.user.is_authenticated:
		return redirect("uwelcome")
	elif request.method == "POST":
		un = request.POST.get("un")
		pw = request.POST.get("pw")
		ur = authenticate(username = un, password = pw)
		if ur is not None:
			login(request, ur)
			return redirect("uwelcome")
		else:
			return render(request, "home.html", {"msg":"Invalid Login"})
	else:
		return render(request, "home.html")

def usignup(request):
	if request.method == "POST":
		un = request.POST.get("un")
		try:
			ur = User.objects.get(username=un)
			return render(request, "signup.html", {"msg":"user already exists"})		
		except User.DoesNotExist:
			text = "0123456789abcdefghijklmnopqrstuvwxyz@#*"
			pw = ""
			for i in range(5):
				pw = pw + text[randrange(len(text))]
			print(pw)
			ur = User.objects.create_user(username=un, password=pw)
			ur.save()
			send_mail("welcome", "Your password is " + str(pw), "bbangtang130613@gmail.com", [str(un)])
			return redirect("home")
	else:
		return render(request, "signup.html")

def urnpassword(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			un = request.POST.get("un")	
			try:
				ur = User.objects.get(username=un)
				text = "0123456789abcdefghijklmnopqrstuvwxyz@#*"
				pw = ""
				for i in range(5):
					pw = pw + text[randrange(len(text))]
				print(pw)
				ur.set_password(pw)
				ur.save()
				send_mail("welcome", "Your password is " + str(pw), "bbangtang130613@gmail.com", [str(un)])
				return redirect("home")
			except User.DoesNotExist:
				return render(request, "rnpassword.html", {"msg":"User doesnot exists"})
		else:
			return render(request, "rnpassword.html")
	else:
		return redirect("home.html")

def uwelcome(request):
	if request.user.is_authenticated:
		data = TripModel.objects.all()
		return render(request, "welcome.html", {"data":data})
	else:
		return redirect("home")

def ulogout(request):
	logout(request)
	return redirect("home")

def remove(request, id):
	st = TripModel.objects.get(srno=id)
	st.Pic.delete()
	st.delete()
	return redirect("home")

def create(request):
	if request.method == "POST":
		data = TripForm(request.POST, request.FILES)
		if data.is_valid():
			data.save()
			msg = "Trip Added"
			fm = TripForm()	
			return render(request, "create.html", {"fm":fm, "msg":msg})
		else:
			msg = "Check Error"
			return render(request, "create.html", {"fm":data, "msg":msg})
	else:
		fm = TripForm()	
		return render(request, "create.html", {"fm":fm})

def result(request, id):
	data = TripModel.objects.get(srno=id)
	return render(request, "result.html", {"data":data})

def place(request):
	if request.method == "POST":
		city = request.POST.get("city")
		try:
			loc = geocoder.osm(city)
			lat = loc.lat
			lng = loc.lng
			lat_lng = [lat, lng]
			f = folium.Figure(width=600, height=600)
			ct = folium.Map(location=lat_lng, zoom_start=13).add_to(f)
			folium.Marker(lat_lng, tool_tip="home").add_to(ct)
			ct_html = ct._repr_html_()
			return render(request, "place.html", {"msg":ct_html})		
		except Exception as e:
			msg = "issue" + str(e)
			return render(request, "place.html", {"msg":msg})
	else:
		return render(request, "place.html")
