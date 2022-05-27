import json

dates = '''
    [{
        "id" : "007",
        "x" : "2",
        "name" : "noe"
    },
    {
        "id" : "009",
        "x" : "7",
        "name" : "daniel"
    }]'''

info = json.loads(dates)
print("User count:",len(info))
for line in info:
    print("Name",line["name"])
print(json.dumps(info,indent=4))