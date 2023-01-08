from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
def emp_data_view_json1(request):
	data={'eid':123,'ename':"venky","eage":23,"eaddress":"Bangalore"}
	response=json.dumps(data)
	return HttpResponse(response,content_type='application/json')

from django.http import JsonResponse
def emp_data_view_json2(request):
	data={'eno':40,'ename':'suhas','eage':'22','eaddress':'Mysore'}
	response=data
	return JsonResponse(response)