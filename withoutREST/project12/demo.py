import requests

BASE_URL='http://127.0.0.1:8000/'
END_POINT='api/'

import json
def create_resource():
	eno=int(input('Enter the Employee number:\t'))
	ename=input('Enter the Name of the Employee:\t')
	esalary=int(input('Enter the salary of the Employee:\t'))
	eaddress=input('Enter the Address of the Employee:\t')
	emp_data={'eno':eno,'ename':ename,'esalary':esalary,'eaddress':eaddress}

	response = requests.post(BASE_URL+END_POINT)
	print(response.json())

create_resource()

