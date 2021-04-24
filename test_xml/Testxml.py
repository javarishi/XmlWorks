'''
Created on 24-Apr-2021

@author: Rishi
'''
from xml.dom import minidom

filepath = "/RISHI/H2K/FileIO/xml/staff.xml"

data = minidom.parse(filepath)

name = data.getElementsByTagName("name")[0]
print(name.firstChild.data)

employees = data.getElementsByTagName("emp")

for eachEmp in employees:
    nickname = eachEmp.getElementsByTagName("nickname")[0]
    salary = eachEmp.getElementsByTagName("salary")[0]
    emp_id = eachEmp.getAttribute("id")
       
    print(emp_id, nickname.firstChild.data, salary.firstChild.data)
    
    
    
    