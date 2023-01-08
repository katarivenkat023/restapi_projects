from django.core.serializers import serialize
import json

class Serializemixin(object):
	def serialize(self,query_string):
		json_data=serialize('json',query_string)
		dict_data=json.loads(json_data)
		complte_list_of_data=[]

		for d in dict_data:
			emp_data=d['fields']
			complte_list_of_data.append(emp_data)
		json_data=json.dumps(complte_list_of_data)
		return json_data