import xml.etree.ElementTree as ET

dates = '''
<person>
<name>Noe</name>
<number type = "intl">8112599353</number>
<email hide = "yes"/>
</person>
'''

tree  = ET.fromstring(dates)
print("name:",tree.find('name').text)