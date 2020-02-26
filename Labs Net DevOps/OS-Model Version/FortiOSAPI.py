import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
class Fortinet(object):

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.__username = ''
        self.__secretkey = ''
        self.url = 'https://%s:%d/'%(self.host, self.port)
        self.verify = False
        self.token = self.token()
        #request URL parameter by GET Method
        self._params = {'access_token':self.token}

    def token(self):
        session = requests.Session()
        #First Login authen by administrator user/passwd
        login_authen = {
            'username': self.__username,
            'secretkey': self.__secretkey
        }
        session.post('https://{}:{}/logincheck'.format(self.host,self.port),
                         data=login_authen,verify=self.verify)
        session.headers.update({'X-CSRFTOKEN': key.value[1:-1] for key in session.cookies if key.name == 'ccsrftoken'})
        #API Token generate
        api_auth = {'api-user': 'api_python'}
        result = session.post('https://{}:{}/api/v2/monitor/system/api-user/generate-key'.format(self.host,self.port),
                         data=json.dumps(api_auth),verify=self.verify).json()
        token = result['results']['access_token']
        #Logout session
        session.get('https://{}:{}/logout'.format(self.host,self.port),verify=self.verify)
        return token

    def monitorapi(self,path,params):
        result = requests.get(url=self.url+path,params=params,verify=self.verify)
        return result

    def resource(self):
        path = 'api/v2/monitor/system/resource/usage'
        reslut = self.monitorapi(path,self._params)
        print(reslut.text)

    @property
    def configbackup(self):
        path = 'api/v2/monitor/system/config/backup'
        self._params['scope'] = 'global'
        result = self.monitorapi(path,params=self._params)
        return result.text

if __name__ == '__main__':
    host = ''
    port = 4433
    fgt = Fortinet(host,port)
    fgt.resource()
    with open(r'/data/fgt/config.txt','w') as f:
        f.write(fgt.configbackup)
