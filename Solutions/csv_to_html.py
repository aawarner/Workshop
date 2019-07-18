
TABLE='''\
<html>
<head>
<style>
table, th, td {
  border: 1px solid blue;
  border-collapse: collapse;
}
th, td {
  padding: 5px;
  text-align: left;
}
</style>
</head>
<body>

<h2>Interfaces and IPs</h2>
<p>Populated from dictionary</p>

<table style="width:400px">
  <tr>
    <th>Int Name</th>
    <th colspan="2">IP/Mask</th>
  </tr>
%s
</table>

</body>
</html>'''

ROW='''\
  <tr>
    <td>%(int_name)s</td>
    <td>%(ip)s</td>
    <td>%(netmask)s</td>
  </tr>
  '''

def read_csv(filename):
    '''aquire interface config data from a CSV file'''
    with open (filename,'r') as f:
        rl=f.readlines()
        array=[i.rstrip('\n').split(',') for i in rl]
    return array



def loop_thru_array(filename):
    array=read_csv(filename)
    rows=''
    for i in array:
        int_name,ip,netmask,description,enabled=i
        d={'int_name':int_name,'ip':ip,'netmask':netmask}
        row=ROW%d
        rows=rows+row
    return TABLE%rows



if __name__=='__main__':
    html=loop_thru_array('interfaces.csv')
    with open('table.html','w') as f:
        f.write(html)
