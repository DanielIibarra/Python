from gettext import find
import xml.etree.ElementTree as ET
from matplotlib.pyplot import text

from psutil import users

xml = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Noe</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Daniel</name>
        </user>
    </users>
</stuff>'''
tree = ET.fromstring(xml)
trees = tree.findall("users/user")
print("Usuarios:",len(trees))
for line in trees:
    print("Usuario:",line.get("x"),"Nombre:",line.find("name").text,"Id:",line.find("id").text)

