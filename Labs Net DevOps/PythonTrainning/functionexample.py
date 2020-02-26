#Define data to split
hostnames = ('dca-core-7609-r1', 'dca-core-7609-r2',
            'dca-core-7609-r3', 'dca-core-7609-r3',
            'iad-tra-mx80-r1','iad-tra-mx80-r2'
             )
#Sort de data and split hostnames

def get_role_by_hostname(hostname):
        info = {}
        info['location'] = hostname.split('-')[0]
        info['role'] = hostname.split('-')[1]
        info['model'] = hostname.split('-')[2]
        return info

        #for h in hostname:
            #info = get_role_by_hostname(h)
            #print 'hostname: %s' % h
            #print 'location: %s' % info['location']
            #print 'role:     %s' % info['role']
            #print 'model:    %s' % info['model']

for h in hostname:
        info = get_role_by_hostname(h)
        print('hostname: %s' %h
        print('location: %s' %info['location'])
        print('role:     %s' %info['role'])
        print('model:    %s' %info['model'])
