import requests

BASE_URL='http://127.0.0.1:8000/'
END_POINT='all/'
response=requests.get(BASE_URL+END_POINT)
data=response.json()
print(data) 

response=requests.post(BASE_URL+END_POINT)
data=response.json()
print(data)

response=requests.put(BASE_URL+END_POINT)
data=response.json()
print(data)

response=requests.delete(BASE_URL+END_POINT)
data=response.json()
print(data)