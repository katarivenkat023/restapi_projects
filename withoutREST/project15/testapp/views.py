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

	def delete(self,request,id,*args,**kwargs):
		emp = self.get_object_data_by_id(id)

		if emp is None:
			json_data = json.dumps({'msg':'No matched resource found, updation not possible'})
			return self.render_to_http_response(json_data,status=404)

		empty_data=emp.delete()
		print(empty_data)

		json_data = json.dumps({'msg':'Resource Deleted successfully'})
		return self.render_to_http_response(json_data)