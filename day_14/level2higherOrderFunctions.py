import math
from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map

ups = map(lambda x: x.upper(), countries)

print(list(ups))

squared = map(lambda x: math.sqrt(x), numbers)

print(list(squared))

upnames = map(lambda x: x.upper(), names)

print(list(upnames))

# Filter

nonlands = filter(lambda x: not x.endswith('land'), countries)

print(list(nonlands))

notlsix = filter(lambda x: (len(x) != 6), countries)

print(list(notlsix))

atleastsix = filter(lambda x: len(x)<6, countries)

print(list(atleastsix))

Estarts = filter(lambda x: not x.startswith('E'), countries)

print(list(Estarts))

# Filter & Map

upEstarts = filter(lambda x: not x.startswith('E'), map(lambda x: x.upper(), countries))

print(list(upEstarts))

ls = [3, 4, 'Hello', 'x=y', True, 'Yellow', False, 2]

def get_string_lists(lst):
    def is_string(var):
        return isinstance(var, str)
    return filter(is_string, lst)

strings = get_string_lists(ls)

print(list(strings))

# Reduce

sum = reduce(lambda x, y: x+y, numbers)

print(sum)

def necountries(lst):
    cst =reduce(lambda x, y: '{}, {}'.format(x, y), lst)
    ind = cst.rfind(',')
    newst = cst[:ind] + ' and' + cst[ind+1:]
    st = '{} are north European countries.'.format(newst)
    return st

ctrs = necountries(countries)
print(ctrs)

