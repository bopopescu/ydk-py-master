#import HTTPS/RESTAPI requests & print
import requests
from pprint import pprint

#Define header & Vars / "COMPLETE"
router = {"ip" : "",
     "port" : "",
     "user" : "",
     "pass" : ""}

#Format of retrieve data
headers = {"Accept": "application/yang-data+json"}

#url
u = "https://{}:{}/restconf/data/interfaces/interface-GibabitEthetnet1"
u = u.format(router["ip"], router["port"])
print(u)

#GET/PUT/POST/PATCH/DELETE
r = request.get(u,
headers = headers,
auth(router["user"], router["pass"]),
verify=false)
pprint(r.text)

#
import jason
api_data = r.json()
interfacename = api_model["ietf-interfaces:interface"]["name"]
print interfacename

#
