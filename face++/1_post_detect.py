import requests
from json import JSONDecoder

from rope.base.pyobjectsdef import _AssignVisitor

http_url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
key = "TEJiWsG8jdpOsM-M2lTIX0AIzoRix7Bu"
secret = "OFaZz6bMcyx2p3qqFEqcps131QGSStYy"
filepath = "1.jpg"
"gender,age"

data = {"api_key": key, "api_secret": secret, "return_landmark": "0","return_attributes":"gender,age,emotion,headpose,eyestatus,beauty,skinstatus"}
files = {"image_file": open(filepath, "rb")}
response = requests.post(http_url, data=data, files=files)

req_con = response.content.decode('utf-8')
req_dict = JSONDecoder().decode(req_con)

print('\n *******************************************************')
print('### ALL ### type:',type(req_dict),'len:',len(req_dict))
print(req_dict)

print('\n *******************************************************')
faces=req_dict['faces']
print('### faces ### type list:',type(faces),'len:',len(faces))
print(faces)
getfaces=faces[0]
print('\n')
print('### faces ### type to dict:',type(getfaces),'len:',len(getfaces),'(去掉[]大括号，即从list[0]中提出dict)')
print(getfaces)

print('\n *******************************************************')
attributes=getfaces['attributes']
print('### attributes ### type:',type(attributes),'len:',len(attributes))
print(attributes)
print('\n *******************************************************')

#print('\n image_id: ',req_dict['image_id'])
#print('\n time_used: ',req_dict['time_used'])
#print('\n request_id: ',req_dict['request_id'])
#print('\n faces: ',req_dict['faces'])
#print(getfaces['landmark'])
#face_rectangle=faces['face_rectangle']
#landmark=faces['landmark']
#attributes=faces['attributes']
#print('\n faces_age: ',faces['face_token'])