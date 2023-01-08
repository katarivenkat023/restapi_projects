from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
from django.http import HttpResponse
import json
from django.core.serializers import serialize
from testapp.mixins import MixinHttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from testapp.utils import is_data_json
from testapp.forms import EmployeeForm

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeListCbv(MixinHttpResponse,View):

	def get_object_data_by_id(self,id):
		try:
			emp = Employee.objects.get(id=id)
		except Employee.DoesNotExist:
			emp = None
		return emp
	
	def put(self,request,id,*args,**kwargs):
		emp = self.get_object_data_by_id(id)

		if emp is None:
			json_data = json.dumps({'msg':'No matched resource found, updation not possible'})
			return self.render_to_http_response(json_data,status=404)

		data=request.body
		valid_json_data=is_data_json(data)
		if not valid_json_data:
			json_data=json.dumps({'msg':'Please send the valid json data'})
			return self.render_to_http_response(json_data,status=400)

		#This is the data coming from Python application inorder to update
		provided_data = json.loads(data)

		#this is the data which is been stored within the database
		original_data = {'eno':emp.eno,'ename':emp.ename,'esalary':emp.esalary,'eaddress':emp.eaddress}
		
		print('Data before Updation')
		print(original_data)

		print('Data After updation')
		#Performing updation on the existing original data
		original_data.update(provided_data)
		print(original_data)

		form = EmployeeForm(original_data,instance=emp)
		if form.is_valid():
			form.save(commit=True)
			json_data = json.dumps({'msg':'Resource Updated successfully'})
			return self.render_to_http_response(json_data)

		if form.errors:
			json_data=json.dumps(form.errors)
			return self.render_to_http_response(json_data,status=400)