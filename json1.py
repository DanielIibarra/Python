import json

data = '''{
    "name":"Noe",
    "phone":{"type":"intl","number":"8112599355"},
    "email":{"hide":"yes"}
           }
'''
load = json.loads(data)
print("Name:",load["name"])
print("hide:",load["email"]["hide"])