import json
from faker import Faker
from random import randint


fake=Faker()
#mostly used function in faker libraray
'''print(fake.email())
print(fake.country())
print(fake.address())
print(fake.name())
print(fake.text())
print(fake.latitude(),fake.longitude())
print(fake.url())'''


def input_data(x):
    #dictionary
    student_data={}

    for i in range(0,x):
        student_data[i]={}
        student_data[i]['id']=randint(1,100)
        student_data[i]['name']=fake.name()
        student_data[i]['address']=fake.address()
        student_data[i]['longitude']=str(fake.longitude())
        student_data[i]['latitude']=str(fake.latitude())

    print(student_data)

    with open('student_information.json','w') as f:
        json.dump(student_data,f, indent=2)

def main():
    print('Enter the number of student for which you want to generate data')
    number_of_student=input()
    input_data(int(number_of_student,10))

main()
