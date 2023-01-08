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

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeListCbv(MixinHttpResponse,View):
	def post(self,request,*args,**kwargs):
		data=request.body
		valid_json_data=is_data_json(data)
		if not valid_json_data:
			json_data=json.dumps({'msg':'Please send the valid json data'})
			return self.render_to_http_response(json_data,status=400)

		json_data=json.dumps({'msg':'this is from post method, Sent data is valid'})
		return self.render_to_http_response(json_data)

