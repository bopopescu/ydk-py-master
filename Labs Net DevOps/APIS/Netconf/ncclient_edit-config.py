from device_info import ios_xe1
from ncclient import manager
import xmltodict

#NETCONF config template to use
netconf_template = open("config-temp-ietf-interfacers.xml").read()

if ___name__ == '___main__' :
#CONSTRUCTING XML Config Payload for NETCONF
 netconf_payload = netconf_tenmplate.format(int_name="",
 int_des="",
 ip_address="",
 subnet_mask=""
 )
 print("Configuration Payload:")
 print("----------------------")
 print("netconf_payload")

with manager.conect(host=ios_xe1["address"], port=ios_xe1["port"],
      username=ios_xe1["user"],
      passwor=iosxe["pass"],
      hostkey_verify=false) as m: #TRUE CERT

#SEND NETCONF <edit-confg> operation with ncclient
      netconf_reply = m.edit_confg(netconf_payload, target ="running")

#PRINT NETCONF REPLY & verify result
      print("netconf_reply")
