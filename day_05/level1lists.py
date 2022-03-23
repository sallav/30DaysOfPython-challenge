
list0 = list()

list = ['cake', 'frosting', 'flours', 'candles', 'sugar', 'eggs']

print(len(list))

print(list[0])
print(list[int((len(list)-1)/2)])
print(list[len(list)-1])

mixed_data_types = ['Mickey', 60, 122.5, True, 'Fift Avenue']
print(mixed_data_types)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))

print(it_companies[0])
print(it_companies[int(len(it_companies)/2)])
print(it_companies[len(it_companies)-1])

it_companies[0] = 'Meta'
print(it_companies)

it_companies.append('ABC')

it_companies.insert(int(len(it_companies)/2), 'Hello')
print(it_companies)

it_companies[3] = it_companies[3].upper()
print(it_companies)

print('#; '.join(it_companies))

print('Hello' in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

it_companies = it_companies[3:]
print(it_companies)

it_companies = it_companies[0:3]
print(it_companies)

it_companies = it_companies[:1]+ it_companies[2:]
print(it_companies)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

it_companies.pop(0)
del it_companies[int(len(it_companies)/2)]
it_companies.pop(len(it_companies)-1)
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)

full_stack = front_end.copy()
print(full_stack)

indx = full_stack.index('Redux')
indx += 1
full_stack.insert(indx, 'Python')
indx += 1
full_stack.insert(indx, 'SQL')
print(full_stack)
