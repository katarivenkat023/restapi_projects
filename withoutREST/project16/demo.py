import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'

'''
def get_resource(id=None):

	data = {}
	if id is not None:
		data  = {'id':id}

	response=requests.get(BASE_URL+END_POINT,data = json.dumps(data))
	print(response.status_code)
	print(response.json())

get_resource()
'''

'''
def create_resource():
	eno=int(input('Enter the Employee number:\t'))
	ename=input('Enter the Name of the Employee:\t')
	esalary=int(input('Enter the salary of the Employee:\t'))
	eaddress=input('Enter the Address of the Employee:\t')
	emp_data={'eno':eno,'ename':ename,'esalary':esalary,'eaddress':eaddress}

	response = requests.post(BASE_URL+END_POINT,data=json.dumps(emp_data))
	print(response.status_code)
	print(response.json())

create_resource()
'''

'''
def update_resource(id):
	update_data={'id':id,'esalary':20000,'eaddress':'Mandya'}
	
	response = requests.put(BASE_URL+END_POINT,data=json.dumps(update_data))
	print(response.json())
	print(response.status_code)

update_resource(2)
'''

def delete_resource(id):
	data={'id':id}
	response = requests.delete(BASE_URL+END_POINT,data=json.dumps(data))
	print(response.json())
	print(response.status_code)

delete_resource(2)

