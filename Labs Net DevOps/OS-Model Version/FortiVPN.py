import requests
import urllib3
import json


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Fortinet(object):

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.__username = 'admin'   #Fortigate admin user
        self.__secretkey = 'secretpass' #Fortigate admin passwd
        self.url = 'https://%s:%d/'%(self.host, self.port)
        self.verify = False
        self.token = self.token()
        self._params = {'access_token':self.token}
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded',
                   'Authorization': 'Bearer ' + self.token}
    def token(self):
        session = requests.Session()
        login_authen = {
            'username': self.__username,
            'secretkey': self.__secretkey
        }
        session.post('https://{}:{}/logincheck'.format(self.host,self.port),
                         data=login_authen,verify=self.verify)
        session.headers.update({'X-CSRFTOKEN': key.value[1:-1] for key in session.cookies if key.name == 'ccsrftoken'})
        api_auth = {'api-user': 'api_python'}
        result = session.post('https://{}:{}/api/v2/monitor/system/api-user/generate-key'.format(self.host,self.port),
                         data=json.dumps(api_auth),verify=self.verify).json()
        token = result['results']['access_token']
        session.get('https://{}:{}/logout'.format(self.host,self.port),verify=self.verify)
        return token

    def cmdbapi(self,path,data):
        result = requests.post(url=self.url + path,
                headers=self.headers,data=json.dumps(data),verify=self.verify)
        return result.status_code

    def policy(self,ike_name,dst):
        path_policy = 'api/v2/cmdb/firewall/policy'
        policy = {
            "name": "vpnpolicy",
            "srcintf": [{"name": "lan1"}],
            "dstintf": [{"name": ike_name}],
            "srcaddr": [{"name": "all"}],
            "dstaddr": dst,
            "action": "accept",
            "status": "enable",
            "schedule": "always",
            "service": [{"name": "ALL"}],
            "nat": "disable",
        }
        s = self.cmdbapi(path_policy,policy)
        if s != 200:
            print('policy create failed,error-code:%s'%s)
            return
        print('Task done.')

    def objectroute(self,ike_name,remote_proxy_address):
        path_objectaddress = 'api/v2/cmdb/firewall/address'
        path_rooute = 'api/v2/cmdb/router/static'
        dst = [{'name': addr} for addr in remote_proxy_address]
        if len(remote_proxy_address) >1:
            for address in remote_proxy_address:
                obj = {
                    "name": address,
                    "subnet": address,
                    "type": "ipmask",
                    "fqdn": "string",
                }
                s = self.cmdbapi(path_objectaddress,obj)
                if s != 200:
                    print('objectaddress create failed,error-code:%s'%s)
                    return
                route = {
                      "status": "enable",
                      "dst": address,
                      "distance": 10,
                      "weight": 0,
                      "priority": 0,
                      "device": ike_name
                    }
                s = self.cmdbapi(path_rooute,route)
                if s != 200:
                    print('staticroute create failed,error-code:%s'%s)
                    return
        else:
            obj = {
                "name": remote_proxy_address[0],
                "subnet": remote_proxy_address[0],
                "type": "ipmask",
                "fqdn": "string",
            }
            s = self.cmdbapi(path_objectaddress,obj)
            if s != 200:
                print('objectaddress create failed,error-code:%s'%s)
                return
            route = {
                "seq-num": 0,
                "status": "enable",
                "dst": remote_proxy_address[0],
                "distance": 10,
                "weight": 0,
                "priority": 0,
                "device": ike_name
            }
            s = self.cmdbapi(path_rooute,route)
            if s != 200:
                print('staticroute create failed,error-code:%s'%s)
                return
        self.policy(ike_name,dst)

    def ipsecvpn(self,ike_name,interface,remote_global_addr,pre_key,ipsec_name,
                 remote_proxy_address):
        assert len(remote_proxy_address) >0,'VPN Remote_proxy_address cannot be empty!'
        path = 'api/v2/cmdb/vpn.ipsec/phase1-interface'
        p1 = {
                  "name": ike_name,
                  "type": "static",
                  "interface": interface,
                  "ike-version": "1",
                  "remote-gw": remote_global_addr,
                  "authmethod": "psk",
                  "mode": "main",
                  "proposal": "aes128-sha1",
                  "psksecret": pre_key
                }
        s = self.cmdbapi(path,p1)
        if s != 200:
            print('Ipsec-phase1 create failed,error-code:%s'%s)
            return
        path = 'api/v2/cmdb/vpn.ipsec/phase2-interface'
        p2 = {
            "name": ipsec_name,
            "phase1name": ike_name,
            "proposal": "aes128-sha1",
            "pfs": "enable",
            "dhgrp": "5",
            "replay": "enable",
            "keepalive": "enable",
            "auto-negotiate": "enable"
            }
        s = self.cmdbapi(path,p2)
        if s != 200:
            print('Ipsec-phase2 create failed,error-code:%s'%s)
            return
        self.objectroute(ike_name,remote_proxy_address)

if __name__ == '__main__':
    host = '172.19.30.1' #Fortigate Managament address
    port = 4433 #Fortigate Managament port,default 443
    fgt = Fortinet(host,port)
    fgt.ipsecvpn('ike_test','lan1','10.1.1.1','fortigate','ipsec_test',
                 ['10.2.2.0/24','10.3.3.0/24'])

# 'ike_test' = vpn phase1 ike name
# 'lan1' = vpn outgoing interface
# '10.1.1.1' = remote device wan address
# 'fortigate' = 'pre-share key'
# 'ipsec_test' = vpn phase2 ipsec name
# ['10.2.2.0/24','10.3.3.0/24'] = list include vpn destination encrypted traffic subnet
