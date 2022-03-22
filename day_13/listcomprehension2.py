
# list to list of dictionaries

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

list1 = [val for sub in [val for sub in countries for val in sub] for val in sub]

list2 = [val for val in [val for b in countries for val in b]]

list3 = [{'country: '+ i[0].upper(), 'city: ' + i[1].upper()} for i in [val for sub in [b for b in countries] for val in sub]]

print(list3)

# list to list of concatenated strings

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

namelist = [i[0] + " " + i[1] for i in [val for sub in [i for i in names] for val in sub]]

print(namelist)