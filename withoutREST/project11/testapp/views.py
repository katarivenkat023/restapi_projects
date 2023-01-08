from django.shortcuts import render
from testapp.models import Employee
from django.http import HttpResponse
import json
from django.views.generic import View
#from django.core.serializers import serialize
from testapp.mixins import Serializemixin

class EmployeeCBV(Serializemixin,View):
	def get(self,request,id,*args,**kwargs):
		try:
			qs=Employee.objects.get(id=id)
		except Employee.DoesNotExist:
			json_data=json.dumps({'msg':'the required source is not available'})
		else:
			json_data=self.serialize([qs,])

		return HttpResponse(json_data,content_type = 'application/json')
