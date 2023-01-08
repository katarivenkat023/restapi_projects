from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View

# Create your views here.
class JsonCbv(View):
	def get(self,request,*args,**kwargs):
			data={'eid':123,'ename':"subbu","eage":22,"eaddress":"Hyderabad"}
			return JsonResponse(data)