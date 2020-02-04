from netmiko import ConectHandler
from prrint import pprint
#session
router = {"device_type" : "",
     "host" : "",
     "user" : "",
     "pass" : ""}
#Connect
net_conect = ConectHandler(ip=router["host"]
username=router["user"]
password=router["pass"]
device_type=router["device_type"])

#input/print

interface_cli = net_conect.send_command("show run interface Gig1")
pprint(interface_cli)
