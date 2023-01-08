import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'

def get_resource(id=None):
	data={}
	if id is not None:
		data = {'id':id}
	response = requests.get(BASE_URL+END_POINT,data=json.dumps(data))
	print(response.json())
	print(response.status_code)


def create_resource():
	new_emp = {'eno':11,'ename':'Ashwini','esalary':60000,'eaddress':'bangalore'}

	response = requests.post(BASE_URL+END_POINT,data=json.dumps(new_emp))
	print(response.json())
	print(response.status_code)

create_resource()



