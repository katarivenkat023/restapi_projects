from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
from django.http import HttpResponse
import json
from django.core.serializers import serialize
from testapp.mixins import *

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from testapp.utils import is_data_json
from testapp.forms import EmployeeForm

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCompleteCRUDusingCbv(MixinHttpResponse,SerializeMixin,View):
	def get_object_data_by_id(self, id):
		try:
			emp = Employee.objects.get(id = id)
		except Employee.DoesNotExist:
			emp = None
		return emp

	def get(self,request,*args,**kwargs):
		data = request.body
		#checking whether the data is Json or not
		valid_json_data = is_data_json(data)

		if not valid_json_data:
			json_data = json.dumps({'msg':'Please send the valid json data'})
			return self.render_to_http_response(json_data,status=400)

		#converting Json data into Dictionary
		provided_data = json.loads(data)

		id = provided_data.get('id',None)
		if id is not None:
			emp= self.get_object_data_by_id(id)
			if emp is None:
				json_data = json.dumps({'msg':'The required source is not available'})
				return self.render_to_http_response(json_data,status=404)
			json_data = self.serialize([emp,])
			return self.render_to_http_response(json_data)

		#if the id is None
		query_string = Employee.objects.all()
		json_data = self.serialize(query_string)
		return self.render_to_http_response(json_data)

	def post(self,request,*args,**kwargs):
		data=request.body
		valid_json_data=is_data_json(data)
		if not valid_json_data:
			json_data=json.dumps({'msg':'Please send the valid json data'})
			return self.render_to_http_response(json_data,status=400)

		emp_data = json.loads(data)

		form = EmployeeForm(emp_data)
		if form.is_valid():
			form.save(commit=True)
			json_data = json.dumps({'msg':'Resource created successfully'})
			return self.render_to_http_response(json_data)

		if form.errors:
			json_data=json.dumps(form.errors)
			return self.render_to_http_response(json_data,status=400)

	def put(self,request,*args,**kwargs):
		
		data=request.body
		valid_json_data=is_data_json(data)
		if not valid_json_data:
			json_data=json.dumps({'msg':'Please send the valid json data'})
			return self.render_to_http_response(json_data,status=400)

		#This is the data coming from Python application inorder to update
		provided_data = json.loads(data)

		id=provided_data.get('id',None)

		if id is None:
			json_data=json.dumps({'msg':'To perform Updation id is mandatory....Please Provide the id'})
			return self.render_to_http_response(json_data,status=400)

		emp=self.get_object_data_by_id(id)

		if emp is None:
			json_data = json.dumps({'msg':'The required source is not available'})
			return self.render_to_http_response(json_data,status=404)

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

	def delete(self,request,*args,**kwargs):
		data=request.body
		valid_json_data=is_data_json(data)
		if not valid_json_data:
			json_data=json.dumps({'msg':'Please send the valid json data'})
			return self.render_to_http_response(json_data,status=400)

		#This is the data coming from Python application inorder to update
		provided_data = json.loads(data)

		id=provided_data.get('id',None)

		if id is not None:
			emp = self.get_object_data_by_id(id)
			if emp is None:
				json_data = json.dumps({'msg':'No matched resource found, updation not possible'})
				return self.render_to_http_response(json_data,status=404)
			(status,deleted_item)=emp.delete()
			if status==1:
				json_data=json.dumps({'msg':'Resource deleted successfully'})
				return self.render_to_http_response(json_data)
			json_data=json.dumps({'msg':'Resource not deleted successfully'})
			return self.render_to_http_response(json_data)

		json_data=json.dumps({'msg':'To perform Deletion id is mandatory....Please Provide the id'})
		return self.render_to_http_response(json_data,status=400)




	