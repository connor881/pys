import requests
from json import JSONDecoder



http_url = "https://api-cn.faceplusplus.com/facepp/v3/compare"
key = "TEJiWsG8jdpOsM-M2lTIX0AIzoRix7Bu"
secret = "OFaZz6bMcyx2p3qqFEqcps131QGSStYy"
filepath1 = "1.jpg"
filepath2 = "2.jpg"

data = {"api_key": key, "api_secret": secret}
files = {"image_file1": open(filepath1, "rb"),"image_file2": open(filepath2, "rb")}
response = requests.post(http_url, data=data, files=files)

req_con = response.content.decode('utf-8')
req_dict = JSONDecoder().decode(req_con)

print('\n *******************************************************')
print('### ALL ### type:',type(req_dict),'len:',len(req_dict))
print(req_dict)
print('\n *******************************************************')
print('\nrequest_id:',req_dict['request_id'],'\nimage_id1:',req_dict['image_id1'],'\nimage_id2:',req_dict['image_id2'])
print('### faces1 ###',req_dict['faces1'])
print('### faces2 ###',req_dict['faces1'])
print('\n *******************************************************')
print('### time_used ### ',req_dict['time_used'])
print('### confidence ### ',req_dict['confidence'])
print('### thresholds ### :',req_dict['thresholds'])
print('\n *******************************************************')

