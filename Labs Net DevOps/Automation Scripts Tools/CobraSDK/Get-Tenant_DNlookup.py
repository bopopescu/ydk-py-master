def get_tenant(moDir, name):
  mo = moDir.lookupByDn('uni/tn-{0}'.format(name))
  return mo

  if __name__ == "__main__":
   username = 'admin'
     password = 'Cisco123'
        protocol = 'https'
           host = 'apic'

              apic = '{0}://{1}'.format(protocol, host)
               session = LoginSession(apic, username, password)
                  moDir = MoDirectory(session)
                   moDir.login()

#LOGIN In To apic

session = LoginSession(apic, username, password)
  moDir = MoDirectory(session)
  moDir.login()
