# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import Customer

# Create your views here.
def hello_fun(request):
	#return "Hello world"
	#return HttpResponse("Hello world")
	return HttpResponse("<h1>Hello world</h1>")
def cust(request):
	if request.method=="POST":
		form_data = request.POST
		cust_inst = Customer(name=form_data.get("cust_name"),
			email=form_data.get("cust_email"))
		cust_inst.save()
	return render(request,"customer.html")
