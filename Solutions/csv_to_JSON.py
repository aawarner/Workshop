from json import dumps


def read_csv(filename):
    '''aquire interface config data from a CSV file'''
    with open (filename,'r') as f:
        rl=f.readlines()
        array=[i.rstrip('\n').split(',') for i in rl]
    return array


def int_cfg(int_name,ip,netmask,description,enabled):
    '''return individual interface config'''
    intf={"name": int_name,"description": description,"enabled": enabled,"ietf-ip:ipv4": {"address": [{"ip": ip,"netmask": netmask}]},"ietf-ip:ipv6": {}}
    return intf

def loop_thru_array(filename):
    array=read_csv(filename)
    for i in array:
        int_name,ip,netmask,description,enabled=i
        intf=int_cfg(int_name,ip,netmask,description,enabled)
        print(dumps(intf,indent=2))


if __name__=='__main__':
    loop_thru_array('interfaces.csv')
