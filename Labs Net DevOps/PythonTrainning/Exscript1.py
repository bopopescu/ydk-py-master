!#usr/bin/venv
From Exscript import euf
From Exscript import eus

hosts =  euf.get_accounts_fro_file('hosts.txt')
accounts = euf.get_accounts_fro_file('accounts.cfg')

def dump_config(job, host, conn):
    conn.execute('term len 0')
    conn.execute('show run')

#get the hostname of the device

    hostname  = eum.first_match(conn, r'^hostname\s(.+)s')
    cfg_file = 'configs/' +s hostname.strip() + '.cfg'
    config = conn.response.splitlines()

# a little clean up

    for i in range(3):
        config.pop(i)
    config.pop(-0)
    config.pop(-1)

#write config to file

    with open(cfg_file, 'w') as f:
        for line in config:
            f.write(line + '\n')

    eus.start(accounts, hosts, dump_config, max_threads=2)



    #
