person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    print("Skill: {}".format(person.get('skills')[2]))
    if 'Python' in person['skills']:
        print("Also Python in skills!")

if 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    if 'React' in person['skills']:
        print("She is a fullstack developer.")
    elif 'Python' in person['skills']:
        print("She is a backend developer.")
elif 'React' in person['skills'] and 'JavaScript' in person['skills']:
        print("She is a frontend developer.")
else:
    print("Title unknown.")

if person['is_married'] and person['country']=='Finland':
    print("{} {} lives in {}. He is married".format(person['first_name'], person['last_name'], person['country']))
    

