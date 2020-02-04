#imports

from ncclient import manager
from pprint import pprint
import xmltodict

#Session

router = {"ip" : "ADD"
    "port" : "port"
    "user" : "user"
    "pass" : "user"}

#xml information intersted in

netconf_filter = "" "XML ""

#netconf conection

m = manager.connect(host=router["ip"]
port=router["port"]
username=router["user"]
password=router["pass"]
hostkey_verify=false)

#parse interface
interface_netconf = m.get.config("running", netconf_filter)
interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"], ["data"]
pprint(interface_python)["interfaces"]["interface"]["name"]["#text"]


#
#
#
#
#
#
