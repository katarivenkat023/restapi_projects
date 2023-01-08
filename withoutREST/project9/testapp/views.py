from django.shortcuts import render
from testapp.models import Employee
from django.http import HttpResponse
import json
from django.views.generic import View
from django.core.serializers import serialize


class EmployeeCBV(View):
	def get(self,request,*args,**kwargs):
		emp_query_set=Employee.objects.all()
		json_data=serialize('json',emp_query_set)
		return HttpResponse(json_data,content_type = 'application/json')
