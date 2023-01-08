from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.
class JsonCBV(View):
	def get(self,request,*args,**kwargs):
		data={'msg':'This is from get method'}
		return JsonResponse(data)
	def post(self,request,*args,**kwargs):
		data={'msg':'This is from post method'}
		return JsonResponse(data)

	def put(self,request,*args,**kwargs):
		data={'msg':'This is from put method'}
		return JsonResponse(data)

	def delete(self,request,*args,**kwargs):
		data={'msg':'This is from delete method'}
		return JsonResponse(data)