from device_info import ios_xe1
from ncclient import manager

if ___name__ == '___main__' :
#OPEN NETCONF SESSION WITH DEVICE / PARAMETERS
      with manager.conect(host=ios_xe1["address"], port=ios_xe1["port"],
      username=ios_xe1["user"],
      passwor=iosxe["pass"],
      hostkey_verify=false) as m: #TRUE CERT
#STORES CAPABILITIES
print("Here are NETCONF capabilities!")
for capability in m.server_capabilities:
    print(capabililty)
#IOS XE
