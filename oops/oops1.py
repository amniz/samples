import json
l=json.load(open("inventory.json","r"))
print(type(l))
i=0
while i<3:
    print(l['rice'][i]['name'])
    i+=1
# for k in l:
#     print(k['rice']['name'])