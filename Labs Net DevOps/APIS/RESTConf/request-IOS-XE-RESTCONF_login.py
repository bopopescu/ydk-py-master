import requests

headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}
username = 'cisco'
password = 'cisco_1234!'

#RRESTCONF GET
 result = requests.get('https://192.168.3.1/restconf/data/native/?fields=version;hostname',
    headers=headers, auth=(username, password), verify=False).json()

 print(result)

 #readable human string
result_str = 'My hostname is: {hostname} and I am running IOS XE {version}'.format(hostname=result['Cisco-IOS-XE-native:native']['hostname'], version=result['Cisco-IOS-XE-native:native']['version'])

print(result_str)
