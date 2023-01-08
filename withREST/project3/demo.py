import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'

def update_resource(id):
	update_data =  {'id':id,'esalary':120000,'eaddress':'tumkur'}
	response = requests.put(BASE_URL+END_POINT,data=json.dumps(update_data))
	print(response.json())
	print(response.status_code)
update_resource(2)

'''
def delete_resource(id):
	emp_data={'id':id}
	response = requests.delete(BASE_URL+END_POINT,data=json.dumps(emp_data))
	print(response.json())
	print(response.status_code)
delete_resource(1)
'''


