from django.shortcuts import render
from testapp.models import Employee
from django.http import HttpResponse
import json
from django.views.generic import View

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

class EmployeeCBV(View):
	def get(self,request,id,*args,**kwargs):
		emp=Employee.objects.get(id=id)
		emp_data={
				'eno':emp.eno,
				'ename':emp.ename,
				'esalary':emp.esalary,
				'eaddress':emp.eaddress

		}
		json_data=json.dumps(emp_data)
		return HttpResponse(json_data,content_type = 'application/json')
