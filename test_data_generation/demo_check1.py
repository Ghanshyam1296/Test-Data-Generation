import json

with open('student_information.json') as f:
    data=json.load(f)

for i in data:
    del data[i]['longitude'],data[i]['latitude']

with open('new_student_information.json','w') as f:
    json.dump(data,f, indent=2)

