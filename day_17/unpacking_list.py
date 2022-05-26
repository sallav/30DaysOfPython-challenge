# Unpacking a list:

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

*nordic_countries, es, ru = names

print(nordic_countries)
print(es + " and " + ru)

# Unpacking a dictionary:

dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}

def info(name, country, city, age):
    return (', ').join([name, country, city, str(age)])

print(info(**dct))