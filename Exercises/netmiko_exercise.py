'''
EXERCISE:

Write a program that will log in to your CSR1000v and deploy the below access-list.
Changes should be written to a file called changes.txt.


ip access-list extended python_acl
 remark ACL added by Python
 permit ip any host 1.2.3.4
 permit ip host 1.2.3.4 any
 deny ip any any

 BONUS:

 After deploying the ACL download the startup config and the running config and write them to a file.
 Compare the two files and write the differences to your console.

 HINT!!!
 Use python library difflib to compare the files and print the differences to your console.
'''
