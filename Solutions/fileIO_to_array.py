
from pprint import pprint as pp

def read_csv(filename):
    '''aquire interface config data from a CSV file'''
    with open (filename,'r') as f:
        rl=f.readlines()
        array=[i.rstrip('\n').split(',') for i in rl]
    return array
if __name__ =='__main__':
    array=read_csv('interfaces.csv')
    pp(array)
