from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
import json
from testapp.mixins import MixinHttpResponse


class JsonCbv(MixinHttpResponse,View):
	def get(self,request,*args,**kwargs):
		data={'msg':'This is from get method'}
		json_data=json.dumps(data)
		return self.render_to_http_response(json_data)

	def post(self,request,*args,**kwargs):
		data={'msg':'This is from post method'}
		json_data=json.dumps(data)
		return self.render_to_http_response(json_data)
		
	def put(self,request,*args,**kwargs):
		data={'msg':'This is from put method'}
		json_data=json.dumps(data)
		return self.render_to_http_response(json_data)
		
	def delete(self,request,*args,**kwargs):
		data={'msg':'This is from delete method'}
		json_data=json.dumps(data)
		return self.render_to_http_response(json_data)
				
				