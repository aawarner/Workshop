from json import dumps


def read_csv(filename):
    '''aquire interface config data from a CSV file, use function from previous exercise'''

    return array


def int_cfg(int_name,ip,netmask,description,enabled):
    '''return individual interface config'''
    intf={"name": int_name,"description": description,"enabled": enabled,"ietf-ip:ipv4": {"address": [{"ip": ip,"netmask": netmask}]},"ietf-ip:ipv6": {}}
    return intf

def loop_thru_array(filename):
    array=read_csv(filename)
    for i in array:
        '''1. unpack i into function int_cfg's arguments'''
        '''2. aquire interface JSON data from unpacked arguments and assign to variable 'intf' '''
        print(dumps(intf,indent=2))


if __name__=='__main__':
    '''3. call function to print JSON formatted data from filename interfaces.csv'''
