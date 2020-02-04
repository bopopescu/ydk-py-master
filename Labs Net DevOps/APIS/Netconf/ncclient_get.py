from device_info import ios_xe1
from ncclient import manager
import xmltodict

#NETCONF FILTER TO USE
netconf_filter = open('filter-ietf-interfacers.xml')read()

if ___name__ == '___main__' :
#OPEN NETCONF SESSION WITH DEVICE / PARAMETERS
      with manager.conect(host=ios_xe1["address"], port=ios_xe1["port"],
      username=ios_xe1["user"],
      passwor=iosxe["pass"],
      hostkey_verify=false) as m: #TRUE CERT
#Get retrieve config and state info for interface
      netconf_reply = m.get(netconf_filter)
      #Process the XML and store in useful dictionaries in python
      inf_details = xmltdict.parse(netconf_reply.xml)["rpc-reply"]["data"]
      inf_config = intf_details["interfaces"]["interface"]
      intf_info = intf_details ["interfaces-sate"]["interface"]
      #Report back current state
      print("")
      print("Interface Details:")
      print(" Name: {}".format(intf_config["name"]))
      print(" Description: {}".format(intf_config["desciption"]))
      print(" Type: {}".format(intf_config["type"][]"text"]))
      print(" MAC Adress: {}".format(intf_info["phys-adress"]))
      print(" Packets Input: {}".format(intf_info["statistics"]["in-unicast-pkts"]))
      print(" Packets Output:  {}".format(intf_info["statistics"]["out-unicast-pkts"]))
