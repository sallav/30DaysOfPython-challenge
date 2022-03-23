
dog = dict()

dog['Name'] = 'Trixie'
dog['Color'] = 'Black'
dog['Breed'] = 'Collie'
dog['Legs'] = 'Good'
dog['Age'] = 13

student = {'first_name':'Holly', 'last_name':'Smith', 'gender':'woman', 'age':26, 'marital status':'single', 'skills':['PHP', 'SQL'], 'country':'Sweden', 'city':'Stockholm', 'address':'not known'}

print(len(student))

print(student.get('skills'))
print(type(student.get('skills')))

student['skills'].append('Javascript')
print(student.get('skills'))

print(student.keys())
print(student.values())

lst = student.items()
print(lst)

student.pop('marital status')
student.popitem()
print(student)

del dog