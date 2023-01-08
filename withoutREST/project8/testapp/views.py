from django.shortcuts import render
from testapp.models import Employee
from django.http import HttpResponse
import json
from django.views.generic import View
from django.core.serializers import serialize
# Create your views here.
#class EmployeeCBV(View):
#	def get(self,request,*args,**kwargs):
#		emp=Employee.objects.get(id=1)
#		emp_data={
#				'eno':emp.eno,
#				'eaddress':emp.eaddress
#
#		}
#		json_data=json.dumps(emp_data)
#		return HttpResponse(json_data,content_type = 'application/json')

#Dynamically taking the input from user
class EmployeeCBV(View):
	def get(self,request,id,*args,**kwargs):
		emp=Employee.objects.get(id=id)
		#serialize(format,query,fields)

		
		json_data=serialize('json',[emp,],fields=('eno','ename'))
		return HttpResponse(json_data,content_type = 'application/json')
