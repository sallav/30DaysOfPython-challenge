it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update(['Meta', 'LinkedIn', 'Fujitsu'])
print(it_companies)

it_companies.remove('IBM')
print(it_companies)

it_companies.discard('Oracle')
print(it_companies)

rmvbl = it_companies.pop()
print(rmvbl)
