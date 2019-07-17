
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
    '''aquire interface config data from a CSV file, use function from previous exercise'''

    return array



def loop_thru_array(filename):
    array=read_csv(filename)
    rows=''
    for i in array:
        '''1. unpack list'''
        '''2. assign unpacked list elements to dictionary'''
        '''3. substitute dictionary values into 'ROW' and assign to variable 'row' '''
        rows=rows+row ###concatenates row data into variable rows
    return '''4. substitute 'rows' into TABLE and return TABLE from this function'''



if __name__=='__main__':
    html=loop_thru_array('interfaces.csv')
    '''5. write html data to file named 'table.html' '''
