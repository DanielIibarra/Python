import xml.etree.ElementTree as ET

from numpy import number

dates = '''
<person>
<name>Noe</name>
<number type = "intl">8112599353</number>
<email hide = "yes"/>
</person>
'''

tree  = ET.fromstring(dates)
print("name:",tree.find('name').text)
print("number: ",tree.find("number").text)
print("Email: ",tree.find("email").get("hide"))